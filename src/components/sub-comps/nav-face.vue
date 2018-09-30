<template>
    <div class="nav-face">
        <div @click="faceClicked=!faceClicked" @animationend="faceClicked=!faceClicked" :class="[faceClicked?'face-icon-clicked':'','face-icon']">
            <img src="@/assets/images/face.png" alt="">
        </div>
    </div>
</template>
<script>
    export default{
        name:'nav-face',
        data(){
            return{
                faceClicked:false
            }
        }
    }
</script>
<style lang="scss" scoped>
    .nav-face{
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
    .face-icon-clicked{
        -webkit-animation: rotateAni 5s 1;
        -moz-animation:    rotateAni 5s 1;
        -o-animation:      rotateAni 5s 1;
        animation:         rotateAni 5s 1; 
    }

    @keyframes rotateAni {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }
</style>