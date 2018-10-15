<template>
    <div class="article-detail">
        <conArticle :articleCon="articleCon"/>
    </div>
</template>
<script>
    import conArticle from '@/components/sub-comps/con-article.vue'
    import {mapActions,mapState} from 'vuex'
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
          this.$store.dispatch('setArticleData',this.$route.params.article_id)
        },
        watch:{
            articleCon(val){
                this.articleCon = val
            }
        }
    }
</script>
<style lang="scss">

</style>