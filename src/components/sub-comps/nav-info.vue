<template>
    <div class="nav-info">
        <h3 class="name">白河夜船</h3>
        <navList />
    </div>
</template>
<script>
    import navList from './nav-list.vue'
    export default{
        name:'nav-info',
        components:{
            navList
        }
    }
</script>
<style lang="scss">
    .nav-info{
        margin-top:30px;
        .name{
            text-align:center;
            font-size:30px;
        }
    }
</style>