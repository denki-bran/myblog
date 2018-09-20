<template>
    <div class="nav-list">
        <ul class="nav-ul">
            <li @mouseover="hover=0" class="nav-item">
                <a href="javascript:;">
                    形 | Skill
                </a>
            </li>
            <li @mouseover="hover=1" class="nav-item">
                <a href="javascript:;">
                    影 | Create
                </a>
            </li>
            <li @mouseover="hover=2" class="nav-item">
                <a href="javascript:;">
                    神 | Life
                </a>
            </li>
            <li @mouseover="hover=3" class="nav-item">
                <a href="javascript:;">
                    荒原 | Index
                </a>
            </li>
        </ul>
    </div>
</template>
<script>
    export default{
        name:'nav-info',
        data(){
            return{
                hover:-1
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