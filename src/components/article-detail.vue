<template>
    <div class="article-detail">
        <conArticle :articleCon="articleCon"/>
    </div>
</template>
<script>
    import conArticle from '@/components/sub-comps/con-article.vue'
    import {mapState} from 'vuex'
    export default{
        name:'article-detail',
        data(){
           return{
           } 
        },
        components:{
            conArticle
        },
        computed: {
          ...mapState({
            articleCon: state => state.indexData.articleDetail,
          })
        },
        created () {
            this.$store.dispatch('setPageStatus',1)
            this.$store.dispatch('setArticleData',this.$route.params.article_id)
        },
        watch:{
            articleCon(val){
                this.$store.dispatch('setPageStatus',2)
                this.articleCon = val
            }
        }
    }
</script>
<style lang="scss">

</style>