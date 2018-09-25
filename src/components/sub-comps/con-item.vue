<template>
    <div class="con-item">
        <div class="con-item-head clearfix con-el">
            <h2 @click='enterArticle' class="item-head-title">{{itmData.title}}</h2>
            <h3 class="item-head-time">{{itmData.date}}</h3>
        </div>
        <div class="con-item-desc con-el">
            <p v-for="(para,idx) in itmData.desc" :key="idx">{{para}}</p>
        </div>
        <div class="con-item-foot con-el clearfix">
            <section class="tag tag-main">
                <span class="tag-type">世界</span>
                <a href="javascript:;" class="tag-name">
                    {{itmData.bigtag.name}}
                </a>
            </section>
            <section class="tag">
                <span class="tag-type">路标</span>
                <a href="javascript:;" class="tag-name" v-for="(tag,idx) in itmData.tags" :key="idx">
                    {{tag.name}}
                </a>
            </section>
        </div>
    </div>
</template>
<script>
    export default{
        name:'con-item',
        data(){
            return{
                // itmData:{
                //   "title": "严西群万集见光则极导认及变很记回验改委志气听次律市",
                //   "date": "2010-08-04",
                //   "desc": [
                //     "验位万能于放往表际目影前。下还他委间点区再光想打复装属候图。器听所设青表权资到县各被民林员书者会。按类区选除统心百为名标上知所育料。积温老织装得个命县石部团志她的格。",
                //     "派青织好半常图清任安般商动满山维。适史然外打去进土般同业七信。带且议分件最识转热向市联。般江重现影油率小品十维史地。音有选率才己列么合习与平光到。",
                //     "有接空压命完角整能斗油正查江它。不性飞包市向革该将委事例眼太说称。就办使调全便给化经可二性用局研。",
                //     "际加名复计史风叫认权被几较代种要例。史受没地共建点原离管月毛起效直很。到记长平支取育式命感采北么难地。我酸她管命主活众政识志表数己反济向。门只据教即如组解就快队段矿十。",
                //     "产十精存三要更断知设对群组。调何又信意把求音后它众或养个。越很全见得参非东导再置其样想理备。她工研运到百选度此接为出是外。而山走清历第便也交他眼任水。"
                //   ],
                //   "bigtag": {
                //     "name": "形",
                //     "href": "/xing"
                //   },
                //   "tags": [
                //     {
                //       "name": "三信流花",
                //       "href": "/zbnc"
                //     },
                //     {
                //       "name": "头同",
                //       "href": "/pixjcuf"
                //     },
                //     {
                //       "name": "会通传",
                //       "href": "/vrwhqwb"
                //     },
                //     {
                //       "name": "和更明",
                //       "href": "/jwrnc"
                //     }
                //   ]
                // }
            }
        },
        props: {
          itmData: Object
        },
        methods:{
            enterArticle: function(){
                
            }
        }
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
    .con-item-desc{
        padding: 16px 24px;
         border-bottom:1px solid #e5e5e5;
         p{
            margin-bottom:10px;
            font-size:16px;
            &:last-child{
                margin-bottom:0;
            }
         }
    }
    .con-item-foot{
        padding: 12px 24px;
    }
    .tag{
        float:left;
        margin-right:20px;
    }
    .tag-type{
        display:inline-block;
        padding:0 5px;
        background-color:#42b983;
        color:#ffffff;
        height:22px;
        line-height:22px;
        border:1px solid #42b983;
        font-size:14px;
    }
    .tag-main{
        .tag-type{
            background-color:#0099ff;
            border-color:#0099ff;
        }
    }
    .tag-name{
        display:inline-block;
        height:22px;
       background-color: #fafafa;
        border-right: 1px solid #c5c5c5;
        border-top: 1px solid #dadada;
        border-bottom: 1px solid #d2d2d2;
        line-height:22px;
        font-size:14px;
        padding:0 5px;
        &:hover{
            text-decoration:none;
        }
    }
</style>