<template>
    <div class="tag-article">

        <conItem v-for="(itm,idx) in listData" :key="idx" :itmData="itm"/>
    </div>
</template>
<script>
    import conItem from '@/components/sub-comps/con-item.vue'
    import conTagItem from '@/components/sub-comps/con-tagitem.vue'
    import {mapState,mapGetters} from 'vuex'
    export default{
        name:'tag-article',
        components:{
            conItem,
            conTagItem
        },
        computed: {
          ...mapState({
            listData: state => state.indexData.flowResult,
          }),
          ...mapGetters({
            cur_tag:'getCurrentTag'
          }),
            tag_id () {
              return this.$route.params.tag_id
            }
        },
        created () {
            this.$store.dispatch('setPageStatus',1)
            this.$store.dispatch('setTagtoArticleData',this.tag_id)
        },
        watch:{
            listData(val){
                this.$store.dispatch('setPageStatus',2)
                this.listData = val
            }
        }
    }
</script>
<style lang="scss">
    .tag-article{
        box-sizing:border-box;
        margin:0 30px;
    }
</style>