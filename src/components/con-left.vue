<template>
    <div class="con-left">
        <navBar/>
    </div>
</template>
<script>
    import navBar from '@/components/nav-bar.vue'
    export default{
        name:'con-left',
        components:{
            navBar
        }
    }
</script>
<style lang="scss">
    .con-left{
        position:fixed;
        left:0;
        top:0;
        height:100%;
        width:300px;
    }
</style>