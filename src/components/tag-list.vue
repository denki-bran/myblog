<template>
    <div class="tag-list">
        <div class="tag-wrapper clearfix">
            <conTagItem v-for="(itm,idx) in tagListData" :key="idx" :tagData="itm"/>
        </div>
    </div>
</template>
<script>
    import conTagItem from '@/components/sub-comps/con-tagitem.vue'
    import {mapState} from 'vuex'
    export default{
        name:'tag-list',
        components:{
            conTagItem
        },
        computed: {
          ...mapState({
            tagListData: state => state.indexData.TagList,
          })
        },
        created () {
            this.$store.dispatch('setPageStatus',1)
            this.$store.dispatch('setTagList')
        },
        watch:{
            tagListData(val){
                this.$store.dispatch('setPageStatus',2)
                this.tagListData = val
            }
        }
    }
</script>
<style lang="scss">
    .tag-list{
        background-color:#ffffff;
        margin:30px;
        border-radius:10px;
        padding:20px;
        box-sizing:border-box;
    }
</style>