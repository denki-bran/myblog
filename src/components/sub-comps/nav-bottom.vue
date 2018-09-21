<template>
    <div class="nav-bottom">
        <p class="nav-sentence-con">{{idx}}</p>
        <p class="nav-sentence-from">————{{from}}</p>
    </div>
</template>
<script>
    export default{
        name:'nav-bottom',
        data(){
            return{
                "sentence": {
                    "xing": {
                        "idx": 0, 
                        "from": "形赠影", 
                        "con": [
                            "天地長不沒，山川無改時", 
                            " 草木得常理，霜露榮悴之", 
                            " 謂人最靈智，獨復不如茲", 
                            " 適見在世中，奄去靡歸期", 
                            " 奚覺無一人，親識豈相思", 
                            " 但餘平生物，舉目情淒洏", 
                            " 我無騰化術，必爾不復疑", 
                            " 願君取吾言，得酒莫苟辭"
                        ]
                    }, 
                    "ying": {
                        "idx": 1, 
                        "from": "影答形", 
                        "con": [
                            "存生不可言，衛生每苦拙", 
                            "誠願遊昆華，邈然茲道絕", 
                            "與子相遇來，未嘗異悲悅", 
                            "憩蔭若暫乖，止日終不別", 
                            "此同既難常，黯爾俱時滅", 
                            "身沒名亦盡，念之五情熱", 
                            "立善有遺愛，胡為不自竭", 
                            "酒雲能消憂，方此詎不劣"
                        ]
                    }, 
                    "shen": {
                        "idx": 2, 
                        "from": "神釋", 
                        "con": [
                            "大鈞無私力，萬理自森著", 
                            "人為三才中，豈不以我故", 
                            "與君雖異物，生而相依附", 
                            "結托既喜同，安得不相語", 
                            "三皇大聖人，今復在何處", 
                            "彭祖愛永年，欲留不得住", 
                            "老少同一死，賢愚無復數", 
                            "日醉或能忘，將非促齡具", 
                            "立善常所欣，誰當為汝譽", 
                            "甚念傷吾生，正宜委運去", 
                            "縱浪大化中，不喜亦不懼", 
                            "應盡便須盡，無復獨多慮"
                        ]
                    }, 
                    "index": {
                        "idx": 3, 
                        "from": "断章", 
                        "con": [
                            "白鳥泊微瀾，沙濁春江缓", 
                            "捕雨夢一斛，好貯霓燈滿", 
                            "持之勸人歌，且誄山川遠", 
                            "空牆久不言，枯燃玻璃盏", 
                            "大城鱗皴久，嵯峨巨骨成", 
                            "燒結鵰翎色，荒穢四極冰", 
                            "醉者濡羽翼，遙舉誓於征", 
                            "摘雲調玉屑，蹕路捕白鯨", 
                            "物誘誠可噬，癮脫亦能烹", 
                            "子彈沒於鏡，時針漾其聲"
                        ]
                    }
                }
            }
        },
        methods:{
            getFrom(idx){
                if(idx==0){
                    return this.sentence.xing.from
                }
                else if(idx==1){
                    return this.sentence.ying.from
                }
                else if(idx==2){
                    return this.sentence.shen.from

                }
                else if(idx==3){
                    return this.sentence.index.from
                }
            },
            getSentence(idx){
                if(idx==0){
                    return this.getRdm(this.sentence.xing.con);
                }
                else if(idx==1){
                    return this.getRdm(this.sentence.ying.con);
                }
                else if(idx==2){
                    return this.getRdm(this.sentence.shen.con);

                }
                else if(idx==3){
                    return this.getRdm(this.sentence.index.con);
                }
            },
            getRdm(arr){
                return arr[Math.floor(Math.random()*arr.length)];
            }
        },
        computed:{
            idx(){
                return this.getSentence(this.$store.state.navBarStore.hoverSec)
            },
            from(){
                return this.getFrom(this.$store.state.navBarStore.hoverSec)
            }
        }
    }
</script>
<style lang="scss">
    .nav-bottom{
        position:absolute;
        bottom:0;
        width:100%;
        height:60px;
        box-sizing:border-box;
        padding:0 30px;
        p{
            font-style:italic;
        }
        .nav-sentence-con{
            text-align:left;
        }
        .nav-sentence-from{
            text-align:right;
        }
    }
</style>