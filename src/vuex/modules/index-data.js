import axios from 'axios'
const PORT = 30129
const API = `http://45.77.152.205:${PORT}/api`
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
        articleDetail:null,
        pageOnLoading:1
            },
    mutations: {
        saveIndexData(state, data) {
            state.flowResult = data;
        },
        saveArticleData(state,data){
            state.articleDetail = data;
        },
        savePageLoadingState(state,data){
            state.pageOnLoading = data;
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
            })
            .catch(function(err){
            })
        },
        setArticleData({commit},article_id) {
            axios({
            url: `${API}${URL.ArticleAPI}/${article_id}`,
            method: 'get',
            timeout: 10000
          })
            .then(function (res) {
                commit('saveArticleData', res.data.con[0])
            })
            .catch(function(err){
            })
        },
        initArticleData({commit}) {
            commit('saveArticleData',null)
        },
        setPageLoadingState({commit},state_flag){
            commit('savePageLoadingState',state_flag)
        }   
    }
}

export default indexData