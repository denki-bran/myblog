<template>
    <div class="mid-list">
        <conItem v-for="(itm,idx) in listData" :key="idx" :itmData="itm"/>
    </div>
</template>
<script>
    import conItem from '@/components/sub-comps/con-item.vue'
    import {mapActions,mapState} from 'vuex'
    export default{
        name:'mid-list',
        components:{
            conItem
        },
        computed: {
          ...mapState({
            listData: state => state.indexData.flowResult,
          })
        },
        created () {
          this.$store.dispatch('setIndexData')
          this.$store.dispatch('initArticleData')
        },
        watch:{
            listData(val){
                this.$store.dispatch('setPageLoadingState',2)
                this.listData = val
            }
        }
    }
</script>
<style lang="scss">
    .mid-list{
        box-sizing:border-box;
        margin:0 30px;
    }
</style>