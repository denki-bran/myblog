<template>
    <div class="con-tagitem">
        <a href="javascript:;" @click='enterTag(tagData.tag_id,tagData.tag_name)'>
            <section class="tag tag-main">
                <span class="tag-type">{{tagData.tag_name}}</span>
                <div class="tag-name">
                    {{tagData.tag_use_num}}
                </div>
            </section>
        </a>
    </div>
</template>
<script>
    export default{
        name:'con-tagitem',
        props: {
          tagData: Object
        },
        methods:{
            enterTag:function(tag_id,tag_name){
                let tag_obj={
                    "tag_name":tag_name,
                    "tag_id":tag_id
                }
                this.$store.dispatch('setCurrentTag',tag_obj)
                this.$router.push({path:`/tag/${tag_id}`})
            }        
        }
    }
</script>
<style lang="scss" scoped>

    
</style>