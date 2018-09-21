<template>
    <div class="con-item">
        <div class="con-item-head clearfix con-el">
            <h2 class="item-head-title">标题测试</h2>
            <h3 class="item-head-time">2018-09-21</h3>
        </div>

        <div class="con-item-body con-el">
            
        </div>
        <div class="con-item-foot con-el">
            
        </div>
    </div>
</template>
<script>
    export default{
        name:'con-item'
    }
</script>
<style lang="scss" scoped>
    .con-item{
        background-color:#ffffff;
        margin:30px 0;
    }
    .con-el{
        padding:0 24px;
    }
    .con-item-head{
        
        box-sizing:border-box;
        height:50px;
        line-height:50px;
        border-bottom:1px solid #e5e5e5;
        h2,h3{
            font-weight:normal;
            
        }
        .item-head-title{
            width:80%;
            float:left;
            font-size:26px;
            text-align:left;
            height:100%;
            overflow:hidden;
        }
        .item-head-time{
            float:right;
            font-size:14px;
            width:20%;
            text-align:right;
            height:100%;
            overflow:hidden;
        }
    }
    .con-item-body{

    }
</style>