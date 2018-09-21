<template>
    <div class="con-mid">
        <midList/>
    </div>
</template>
<script>
    import midList from '@/components/mid-list.vue'
    export default{
        name:'con-mid',
        components:{
            midList
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