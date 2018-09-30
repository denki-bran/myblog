"""
Main function.
"""

__author__ = "Aaron Tei"
__email__ = "dd7217918@gmail.com"
__name__ = "__mktab__"

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'BLOG'

config={
        'user':'',
        'password':'',
        'host':'localhost',
        'port':3306,
        'charset':'utf8'
    }

TABLES ={}
TABLES['article'] = (
    "CREATE TABLE `Article` ("
    "  `article_id` varchar(20) NOT NULL,"
    "  `article_title` varchar(100) NOT NULL,"
    "  `article_desc` varchar(300) NOT NULL,"
    "  `article_time` datetime NOT NULL,"
    "  `article_bigtag_id` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`article_id`)"
    ") ENGINE=InnoDB")

TABLES['article_detail'] = (
    "CREATE TABLE `Article_Detail` ("
    "  `article_id` varchar(20) NOT NULL,"
    "  `article_title` varchar(100) NOT NULL,"
    "  `article_desc` varchar(300) NOT NULL,"
    "  `article_detail` varchar(20000) NOT NULL,"
    "  `article_view_num` int(11) NOT NULL DEFAULT 0,"
    "  `article_time` datetime NOT NULL,"
    "  `article_bigtag_id` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`article_id`)"
    ") ENGINE=InnoDB")

TABLES['big_tag'] = (
    "CREATE TABLE `Big_Tag` ("
    "  `big_tag_id` varchar(20) NOT NULL,"
    "  `big_tag_name` varchar(100) NOT NULL,"
    "  `big_tag_href` varchar(300) NOT NULL,"
    "  `big_tag_use_num` int(11) NOT NULL DEFAULT 0,"
    "  PRIMARY KEY (`big_tag_id`)"
    ") ENGINE=InnoDB")

TABLES['tag'] = (
    "CREATE TABLE `Tag` ("
    "  `tag_id` varchar(20) NOT NULL,"
    "  `tag_name` varchar(100) NOT NULL,"
    "  `tag_href` varchar(300) NOT NULL,"
    "  `tag_use_num` int(11) NOT NULL DEFAULT 0,"
    "  PRIMARY KEY (`tag_id`)"
    ") ENGINE=InnoDB")

TABLES['tag_relationship'] = (
    "CREATE TABLE `Tag_Relationship` ("
    "  `tag_relationship_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tag_id` varchar(20) NOT NULL,"
    "  `article_id` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`tag_relationship_id`)"
    ") ENGINE=InnoDB")

conn = mysql.connector.connect(**config)
cursor = conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    conn.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        conn.database = DB_NAME
    else:
        print(err)
        exit(1)
for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
conn.close()