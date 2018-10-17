<template>
    <div class="con-item">
        <div class="con-item-head clearfix con-el">
            <a @click='enterArticle(itmData.article_id)' class="item-head-title" href="javascript:;">{{itmData.article_title}}</a>
            <h3 class="item-head-time">{{itmData.article_time}}</h3>
        </div>
        <div class="con-item-desc con-el" v-html="itmData.article_desc">

            <!-- <p v-for="(para,idx) in itmData.article_desc" :key="idx">{{para}}</p> -->
        </div>
        <div class="con-item-foot con-el clearfix">
            <section class="tag tag-main">
                <span class="tag-type">世界</span>
                <a href="javascript:;" @click='enterCat(itmData.bigtag.big_tag_href)' class="tag-name">
                    {{itmData.bigtag.big_tag_name}}
                </a>
            </section>
            <section class="tag">
                <span class="tag-type">路标</span>
                <a href="javascript:;" @click='enterTag(tag.tag_id)' class="tag-name" v-for="(tag,idx) in itmData.tags" :key="idx">
                    {{tag.tag_name}}
                </a>
            </section>
        </div>
    </div>
</template>
<script>
    export default{
        name:'con-item',
        props: {
          itmData: Object
        },
        methods:{
            enterArticle: function(article_id){
                this.$router.push({path:`/article/${article_id}`})
            },
            enterCat:function(bigtag_href){
                this.$router.push({path:`/cat${bigtag_href}`})
            },
            enterTag:function(tag_id){
                this.$router.push({path:`/tag/${tag_id}`})
            }        
        }
    }
</script>
<style lang="scss" scoped>
    .con-item{
        background-color:#ffffff;
        margin:30px 0;
    }
    .con-el{
        padding:0 24px;
    }
    .con-item-head{
        box-sizing:border-box;
        height:50px;
        line-height:50px;
        border-bottom:1px solid #e5e5e5;
        h2,h3{
            font-weight:normal;
            
        }
        .item-head-title{
            width:80%;
            float:left;
            font-size:26px;
            text-align:left;
            height:100%;
            overflow:hidden;
            cursor:pointer;
            color:#333333;
            &:hover{
                color:#333333;
                text-decoration:none;
            }
        }
        .item-head-time{
            float:right;
            font-size:14px;
            width:20%;
            text-align:right;
            height:100%;
            overflow:hidden;
        }
    }
    .con-item-desc{
        padding: 16px 24px;
         border-bottom:1px solid #e5e5e5;
         p{
            font-size:16px;
            &:last-child{
                margin-bottom:0;
            }
         }
         h1,h2,h3,p,li{
                padding-bottom:10px;
            }
            p,li{
                line-height:1.6em;
            }
    }
    .con-item-foot{
        padding: 12px 24px;
    }
    
</style>