<template>
    <div class="nav-list">
        <ul class="nav-ul">
            <li @mouseover="handleHover(0)" @click="enterCat('skill')" class="nav-item">
                <a href="javascript:;">
                    形 | Skill
                </a>
            </li>
            <li @mouseover="handleHover(1)" @click="enterCat('create')" class="nav-item">
                <a href="javascript:;">
                    影 | Create
                </a>
            </li>
            <li @mouseover="handleHover(2)" @click="enterCat('life')" class="nav-item">
                <a href="javascript:;">
                    神 | Life
                </a>
            </li>
            <li @mouseover="handleHover(3)" @click="enterTagList()" class="nav-item">
                <a href="javascript:;">
                    断章 | Tags
                </a>
            </li>
        </ul>
    </div>
</template>
<script>
    import {mapActions} from 'vuex'
    export default{
        name:'nav-info',
        data(){
            return{
                hover:-1
            }
        },
        methods:{
            ...mapActions(['setChangeState']),
            handleHover(num){
                this.setChangeState({num});
            },
            enterCat(cat){
                let _path = `/cat/${cat}`
                //console.log(_path);
                this.$router.push({path:_path})
            },
            enterIndex(){
                this.$router.push({path:`/`})
            },
            enterTagList(){
                this.$router.push({path:`/taglist`})
            }
        }
    }
</script>
<style lang="scss" scoped>
    .nav-list{
        width:90px;
        margin:20px auto 0 auto;
    }
    .nav-item{
        a{
            text-align:left;
            padding-top:32px;
            display:block;
            width:100%;
            height:24px;
            line-height:24px;
            font-size:16px;
        }
    }
</style>