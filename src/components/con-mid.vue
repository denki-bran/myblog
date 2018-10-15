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