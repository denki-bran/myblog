<template>
    <div class="con-article">
        <section class="article-head">
            <section class="article-title">
                <p>{{articleCon.article_title}}</p>
            </section>
            <section class="article-time">
                <p>{{articleCon.article_time}}</p>
            </section>
            <section class="article-tags">
                <section class="tag tag-main tag-pos">
                    <span class="tag-type">世界</span>
                    <a href="javascript:;" @click='enterCat(articleCon.bigtag.big_tag_href)' class="tag-name">
                        {{articleCon.bigtag.big_tag_name}}
                    </a>
                </section>
                <section class="tag tag-pos">
                    <span class="tag-type">路标</span>
                    <a href="javascript:;" @click='enterTag(tag.tag_href)' class="tag-name" v-for="(tag,idx) in articleCon.tags" :key="idx">
                        {{tag.tag_name}}
                    </a>
                </section>
            </section>
        </section>
        <section class="article-content" v-html="articleCon.article_detail">       
        </section>
    </div>
</template>
<script>
    export default{
        name:'con-article',
        props:{
            articleCon:Object
        },
        methods:{
            enterCat:function(bigtag_href){
                this.$router.push({path:`/cat${bigtag_href}`})
            },
            enterTag:function(tag_href){
                this.$router.push({path:`/tag${tag_href}`})
            }        
        }
    }
</script>
<style lang="scss">
    .con-article{
        background-color:#ffffff;
        margin:30px;
        border-radius:10px;
        padding:20px;
        box-sizing:border-box;
        .tag-pos{
            float:none;
        }
        .article-tags{
            display:flex;
            width:100%;
            box-sizing:border-box;
            justify-content:center;
            padding-top:5px;
        }
        .article-head{
            padding-bottom:20px;
            box-sizing:border-box;
        }
        .article-title{
            padding-bottom:10px;
            p{
                text-align:center;
                font-size:32px;
            }
        }
        .article-time{
            padding-bottom:10px;
            p{
                text-align:center;
            }
        }
        .article-content{
            blockquote{
                padding-top:10px;
                position:relative;
                &:before{
                    content:"";
                    position:absolute;
                    left:-20px;
                    top:0;
                    height:100%;
                    width:3px;
                    background-color:#0099ff;
                }
            }
            h1{
                font-size:28px;
            }
            h2{
                font-size:24px;
            }
            h3{
                font-size:22px;
            }
            h1,h2,h3,p,li{
                padding-bottom:10px;
            }
            p{
                line-height:1.6em;
            }
        }
    }
</style>