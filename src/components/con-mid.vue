<template>
    <div class="con-mid">
        <articleDetail v-if='page === "article"' />
        <tagList v-else-if='page === "taglist"' />
        <tagArticle v-else-if='page === "tag"' />
        <catList v-else-if='match[0].name ==="cat"' />
        <midList v-else/>
    </div>
</template>
<script>
    import midList from '@/components/mid-list.vue'
    import articleDetail from '@/components/article-detail.vue'
    import catList from '@/components/cat-list.vue'
    import tagList from '@/components/tag-list.vue'
    import tagArticle from '@/components/tag-article.vue'
    export default{
        name:'con-mid',
        components:{
            midList,
            articleDetail,
            catList,
            tagList,
            tagArticle
        },
        computed:{
            page () {
              return this.$route.name
            },
            match(){
                return this.$route.matched
            }
        },
        created(){
            this.$store.dispatch('initArticleData')
        }
    }
</script>
<style lang="scss">
    .con-mid{
        position:absolute;
        left:300px;
        min-height:100%;
        width:auto;
        right:0;
    }
    .tag{
        float:left;
        margin: 5px 20px 5px 0;
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