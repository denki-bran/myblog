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
        methods:{
            ...mapActions(['setIndexData','setBigTag'])
        },
        computed: {
          ...mapState({
            listData: state => state.indexData.flowResult,
            BigTag: state=> state.indexData.bigTag
          })
        },
        // mounted () {
        //   this.$store.dispatch('setIndexData')
        // },
        watch:{
            listData(val){
                this.listData = val
            }
        },
        created(){
            this.setBigTag('bigtag_01');
        }
    }
</script>
<style lang="scss">
    .mid-list{
        box-sizing:border-box;
        margin:0 30px;
    }
</style>