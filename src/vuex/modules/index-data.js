import axios from 'axios'
const API = `http://45.77.152.205:5000/api`
const URL = {
    'listAPI':'/simple/list',
    'ArticleAPI':'/articles',
    'BigTagAPI':'/bigtag',
    'TagAPI':'/tags',
    'TagRelationAPI':'/tags_relation'
}

const indexData = {
    state: {
        flowResult: null,
        bigTag:'bigtag_01'
            },
    mutations: {
        saveIndexData(state, data) {
            state.flowResult = data;
        },
        saveBigTag(state, data){
            state.bigTag = data;
        }
    },
    actions: {
        setIndexData({commit}) {
           axios({
            url: `${API}${URL.listAPI}`,
            method: 'get',
            timeout: 10000
          })
            .then(function (res) {
                commit('saveIndexData', res.data.con)
                console.log('1');
            })
            .catch(function(err){
console.log('2');
            })
        },
        setBigTag({commit},bigtag_id){
            axios({
                url: `${API}${URL.BigTagAPI}/${bigtag_id}`,
                method: 'get',
                timeout: 10000
              })
            .then(function (res) {
                //console.log(res.data.con)
                commit('saveBigTag', res.data.con)
            })
            .catch(function(err){

            })
        }
    }
}

export default indexData