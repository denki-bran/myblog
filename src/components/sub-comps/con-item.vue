<template>
    <div class="con-item">
        <div class="con-item-head clearfix con-el">
            <h2 @click='enterArticle(itmData.article_id)' class="item-head-title">{{itmData.article_title}}</h2>
            <h3 class="item-head-time">{{itmData.article_time}}</h3>
        </div>
        <div class="con-item-desc con-el" v-html="itmData.article_desc">

            <!-- <p v-for="(para,idx) in itmData.article_desc" :key="idx">{{para}}</p> -->
        </div>
        <div class="con-item-foot con-el clearfix">
            <section class="tag tag-main">
                <span class="tag-type">世界</span>
                <a href="javascript:;" class="tag-name">
                    {{bigtag}}
                </a>
            </section>
            <section class="tag">
                <span class="tag-type">路标</span>
                <a href="javascript:;" class="tag-name" v-for="(tag,idx) in itmData.tags" :key="idx">
                    {{tag.name}}
                </a>
            </section>
        </div>
    </div>
</template>
<script>
    import {mapActions,mapState} from 'vuex'
    export default{
        name:'con-item',
        props: {
          itmData: Object
        },
        methods:{
            ...mapActions(['setBigTag']),
            enterArticle: function(article_id){
                this.$router.push({path:`/article/${article_id}`})
            }
        },
        computed: {
          ...mapState({
            BigTag: state=> state.indexData.bigTag
          })
        },
        // mounted(){
        //     this.bigtag = this.setBigTag(itmData.article_bigtag_id);
        // }
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
            margin-bottom:10px;
            font-size:16px;
            &:last-child{
                margin-bottom:0;
            }
         }
    }
    .con-item-foot{
        padding: 12px 24px;
    }
    .tag{
        float:left;
        margin-right:20px;
    }
    .tag-type{
        display:inline-block;
        padding:0 5px;
        background-color:#42b983;
        color:#ffffff;
        height:22px;
        line-height:22px;
        border:1px solid #42b983;
        font-size:14px;
    }
    .tag-main{
        .tag-type{
            background-color:#0099ff;
            border-color:#0099ff;
        }
    }
    .tag-name{
        display:inline-block;
        height:22px;
       background-color: #fafafa;
        border-right: 1px solid #c5c5c5;
        border-top: 1px solid #dadada;
        border-bottom: 1px solid #d2d2d2;
        line-height:22px;
        font-size:14px;
        padding:0 5px;
        &:hover{
            text-decoration:none;
        }
    }
</style>