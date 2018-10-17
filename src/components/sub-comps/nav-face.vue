<template>
    <div class="nav-face">
        <div @click='enterIndex()' @animationend="faceClicked=0" :class='setClass()'>
            <img src="@/assets/images/face.png" alt="">
        </div>
    </div>
</template>
<script>
    import { mapGetters } from 'vuex'
    export default{
        name:'nav-face',
        data(){
            return{
                faceClicked:0
            }
        },
        computed: {
          ...mapGetters({
            pageStatus:'getPageStatus'
          })
        },
        methods:{
            faceClickDetect:function(){
                if(this.faceClicked<2){
                    this.faceClicked=this.faceClicked+1
                }
                else{
                    this.faceClicked = 0;
                }
            },
            setClass:function(){
                let classBox = 'face-icon'
                if(this.faceClicked == 0){
                    return classBox;
                }
                else if(this.faceClicked == 1){
                    return classBox+' face-icon-infinite';
                }
                else if(this.faceClicked == 2){
                    return classBox+' face-icon-once';
                }
            },
            enterIndex(){
                this.$router.push({path:`/`})
            }
        },
        watch:{
            pageStatus(val){
                this.faceClicked = val;
            }
        },
        created(){
            this.faceClicked = this.pageStatus;
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
    .face-icon-infinite{
        -webkit-animation: rotateAni 2s infinite linear;
        -moz-animation:    rotateAni 2s infinite linear;
        -o-animation:      rotateAni 2s infinite linear;
        animation:         rotateAni 2s infinite linear; 
    }
    .face-icon-once{
        -webkit-animation: rotateAni 2s 1 linear;
        -moz-animation:    rotateAni 2s 1 linear;
        -o-animation:      rotateAni 2s 1 linear;
        animation:         rotateAni 2s 1 linear; 
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