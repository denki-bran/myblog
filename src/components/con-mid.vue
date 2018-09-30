<template>
    <div class="con-mid">
        <midList v-if='page === "home"'/>
        <articleDetail v-else-if='page === "article"' />
    </div>
</template>
<script>
    import midList from '@/components/mid-list.vue'
    import articleDetail from '@/components/article-detail.vue'
    export default{
        name:'con-mid',
        components:{
            midList,
            articleDetail
        },
        computed:{
            page () {
              return this.$route.name
            }
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
</style>