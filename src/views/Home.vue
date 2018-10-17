<template>
  <div class="home">
    <conLeft/>
    <conMid/>
  </div>
</template>

<script>
import conLeft from '@/components/con-left.vue';
import conMid from '@/components/con-mid.vue';
export default {
    name: 'home',
    components:{
        conLeft,
        conMid
    },
    beforeRouteUpdate (to, from, next) {
        this.$store.dispatch('initListData')
        if(to.params){
            let _params = to.params;
            if(_params.cat_name){
                let _catName = _params.cat_name;
                if(_catName == 'skill'){
                    this.$store.dispatch('setCatData','bigtag_01')
                }
                else if(_catName == 'create'){
                    this.$store.dispatch('setCatData','bigtag_02')
                }
                else if(_catName == 'life'){
                    this.$store.dispatch('setCatData','bigtag_03')
                }
            }
            else if(to.name=='tag'){
                if(_params.tag_id){
                    let _tag_id = _params.tag_id;
                    this.$store.dispatch('setTagtoArticleData',_tag_id)
                }
            }
        }
        next()
    },
    beforeRouteLeave(to, from , next){
        this.$store.dispatch('initListData')
        next()
    }
    // beforeRouteUpdate (to, from, next) {
    //     console.log('change')
    //     this.$router.go(this.$router.currentRoute)
    // }
}
</script>
