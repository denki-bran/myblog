<template>
    <div class="cat-list">
        <conItem v-for="(itm,idx) in listData" :key="idx" :itmData="itm"/>
    </div>
</template>
<script>
    import conItem from '@/components/sub-comps/con-item.vue'
    import {mapState} from 'vuex'
    export default{
        name:'mid-list',
        components:{
            conItem
        },
        computed: {
          ...mapState({
            listData: state => state.indexData.flowResult,
          }),
            page () {
              return this.$route.name
            },
            catName(){
                return this.$route.params.cat_name
            },
            catBigTag(){
                if(this.catName == 'skill'){
                    return 'bigtag_01'
                }
                else if(this.catName == 'create'){
                    return 'bigtag_02'
                }
                else if(this.catName == 'life'){
                    return 'bigtag_03'
                }
            }
        },
        created () {
            this.$store.dispatch('setPageStatus',1)
            this.$store.dispatch('setCatData',this.catBigTag)
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
    .cat-list{
        box-sizing:border-box;
        margin:0 30px;
    }
</style>