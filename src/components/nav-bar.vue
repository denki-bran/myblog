<template>
    <div class="nav-bar">
        <navMask/>
        <navFace/>
        <navInfo/>
        <navBottom/>
    </div>
</template>
<script>
    import navFace from '@/components/sub-comps/nav-face.vue'
    import navMask from '@/components/sub-comps/nav-mask.vue'
    import navInfo from '@/components/sub-comps/nav-info.vue'
    import navBottom from '@/components/sub-comps/nav-bottom.vue'
    export default{
        name:'nav-bar',
        components:{
            navFace,
            navMask,
            navInfo,
            navBottom
        }
    }
</script>
<style lang="scss">
    .nav-bar{
        background-color:#ffffff;
        width:100%;
        height:100%;
    }
</style>