<template>
    <div class="mid-list">
        <conItem/>
    </div>
</template>
<script>
    import conItem from '@/components/sub-comps/con-item.vue'
    export default{
        name:'mid-list',
        components:{
            conItem
        }
    }
</script>
<style lang="scss">
    .mid-list{
        box-sizing:border-box;
        margin:0 30px;
    }
</style>