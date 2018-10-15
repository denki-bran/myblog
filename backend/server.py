"""
Main function.
"""

__author__ = "Aaron Tei"
__email__ = "dd7217918@gmail.com"
__name__ = "__main__"

from flask import Flask, jsonify, abort, request
from  flask_restful import Api, Resource,reqparse
import mysql.connector
import json
from time import strftime,gmtime
from datetime import datetime
from pytz import timezone
import string
import random

app = Flask(__name__)
api = Api(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(DateTimeEncoder, self).default(obj)

def jsonConvert(_list):
    return {'con':_list}

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

def genRdId():
    return (strftime("%Y%m%d%H%M%S",gmtime())+random_string(6))

class ListAPI(Resource):
    def get(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Article ')
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)

class ArticleAPI(Resource):
    def get(self,article_id):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Article_Detail WHERE article_id = %s', (article_id,))
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)

    def delete(self,article_id):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute("SELECT article_bigtag_id FROM Article WHERE article_id=%s", (article_id,))
            rows = cursor.fetchall()
            for itm in rows:
                cursor.execute('UPDATE Big_Tag SET big_tag_use_num=big_tag_use_num-1 WHERE big_tag_id=%s',(itm['article_bigtag_id'],))
            cursor.execute('DELETE FROM Article_Detail WHERE article_id = %s', (article_id,))
            cursor.execute('DELETE FROM Article WHERE article_id = %s', (article_id,))
            cursor.execute("SELECT tag_id FROM Tag_Relationship WHERE article_id=%s", (article_id,))
            rows = cursor.fetchall()
            for itm in rows:
                cursor.execute('UPDATE Tag SET tag_use_num=tag_use_num-1 WHERE tag_id=%s',(itm['tag_id'],))
            cursor.execute('DELETE FROM Tag_Relationship WHERE article_id = %s', (article_id,))
            cursor.execute('DELETE FROM Tag WHERE tag_use_num=0')
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print(e.message)

class ArticlesAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('article_title', type = str, location = 'json',required = True)
        self.reqparse.add_argument('article_desc', type = str, location = 'json',required = True)
        self.reqparse.add_argument('article_detail', type = str, location = 'json',required = True)
        self.reqparse.add_argument('article_bigtag_id', type = str, location = 'json',required = True)
        self.reqparse.add_argument('article_tag', type = list, location = 'json')
        super(ArticlesAPI, self).__init__()

    def get(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Article_Detail')
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return result
                #return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)

    def post(self):
        try:
            _id_Article = genRdId()
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            args = self.reqparse.parse_args()
            dt = datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
            article_tag_list = args['article_tag']
            for item in article_tag_list:
                query = ("SELECT tag_use_num,tag_id FROM Tag WHERE tag_name=%s")
                _name_tag = item
                cursor.execute(query,(_name_tag, ))
                rows = cursor.fetchall()
                if not rows:
                    _id_tag = genRdId()
                    _href_tag='/'+item
                    cursor.execute('INSERT INTO Tag(tag_id,tag_name,tag_href,tag_use_num) VALUES(%s,%s,%s,1)',(_id_tag,_name_tag,_href_tag))
                    conn.commit()
                else:
                    _id_tag = rows[0]['tag_id']
                    cursor.execute('UPDATE Tag SET tag_use_num=tag_use_num+1 WHERE tag_name=%s',(_name_tag,))
                    conn.commit()
                cursor.execute('INSERT INTO Tag_Relationship(tag_id,article_id) VALUES(%s,%s)',(_id_tag,_id_Article))
                conn.commit()
            cursor.execute('INSERT INTO Article_Detail(article_id,article_title,article_desc,article_detail,article_time,article_bigtag_id) VALUES(%s,%s,%s,%s,%s,%s)',(_id_Article,args.article_title,args.article_desc,args.article_detail,dt,args.article_bigtag_id))
            conn.commit()
            cursor.execute('INSERT INTO Article(article_id,article_title,article_desc,article_time,article_bigtag_id) VALUES(%s,%s,%s,%s,%s)',(_id_Article,args.article_title,args.article_desc,dt,args.article_bigtag_id))
            conn.commit()
            cursor.execute('UPDATE Big_Tag SET big_tag_use_num=big_tag_use_num+1 WHERE big_tag_id=%s',(args.article_bigtag_id,))
            conn.commit()
            cursor.execute('SELECT * FROM Article_Detail')
            result=cursor.fetchall()
            print("Articles:")
            for r in result:
                print(r)
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print(e.message)

class BigTagAPI(Resource):
    def get(self,bigtag_id):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Big_Tag WHERE big_tag_id = %s', (bigtag_id,))
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)
    def delete(self,bigtag_id):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('DELETE FROM Big_Tag WHERE bigtag_id = %s', (bigtag_id,))
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print(e.message)

class BigTagsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('big_tag_name', type = str, location = 'json',required = True)
        self.reqparse.add_argument('big_tag_href', type = str, location = 'json',required = True)
        self.reqparse.add_argument('big_tag_id', type = str, location = 'json',required = True)
        super(BigTagsAPI, self).__init__()

    def get(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Big_Tag')
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)

    def post(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            args = self.reqparse.parse_args()
            cursor.execute('INSERT INTO Big_Tag(big_tag_id,big_tag_name,big_tag_href) VALUES(%s,%s,%s)',(args.big_tag_id,args.big_tag_name,args.big_tag_href))
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print(e.message)

class TagAPI(Resource):
    def get(self,tag_name):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Tag WHERE tag_name = %s', (tag_name,))
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)
    def delete(self,tag_name):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('DELETE FROM Big_Tag WHERE tag_name = %s', (tag_name,))
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print(e.message)

class TagsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('big_tag_name', type = str, location = 'json',required = True)
        self.reqparse.add_argument('big_tag_href', type = str, location = 'json',required = True)
        self.reqparse.add_argument('big_tag_id', type = str, location = 'json',required = True)
        super(TagsAPI, self).__init__()

    def get(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Tag')
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)

class TagRelationAPI(Resource):
    def get(self,tag_id):
        try:
            conn = mysql.connector.connect(**config)
            cursor=conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)
            cursor.execute('SELECT * FROM Tag_Relationship WHERE tag_id = %s', (tag_id,))
            columns=cursor.column_names
            result=cursor.fetchall()
            cursor.close()
            conn.close()
            if result == []:
                return []
            else:
                return jsonConvert(json.loads(json.dumps(result, cls=CJsonEncoder)))
        except mysql.connector.Error as e:
            print(e.message)

api.add_resource(ListAPI,'/api/simple/list')#Article

api.add_resource(ArticleAPI,'/api/articles/<article_id>')#Article_Detail
api.add_resource(ArticlesAPI,'/api/articles')#Article_Detail

api.add_resource(BigTagAPI,'/api/bigtag/<bigtag_id>')#Big_Tag
api.add_resource(BigTagsAPI,'/api/bigtag')#Big_Tag

api.add_resource(TagAPI,'/api/tags/<tag_name>')#Tag
api.add_resource(TagsAPI,'/api/tags')#Tag

api.add_resource(TagRelationAPI,'/api/tags_relation/<tag_id>')#Tag_Relationship




if __name__ == '__main__':
    app.run(host='0.0.0.0')
