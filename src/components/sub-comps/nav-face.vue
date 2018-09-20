<template>
    <div class="round-face">
        <div class="face-icon">
            <img src="@/assets/images/face.png" alt="">
        </div>
    </div>
</template>
<script>
    export default{
        name:'round-face',
        data(){
            
        }
    }
</script>
<style lang="scss">
    .round-face{
        width:100%;
        height:120px;
        position:relative;
        padding-top:130px;
    }
    .face-icon{
        height:120px;
        width:120px;
        margin:0 auto;
        border-radius:60px;
        overflow:hidden;
        border: 2px solid transparent;
        img{
            width:120px;
            height:120px;
        }
        &:hover{
            cursor:pointer;
                border: 2px #f44336 solid;
        }
    }
</style>