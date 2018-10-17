import axios from 'axios'
const PORT = 30129
const API = `http://45.77.152.205:${PORT}/api`
const URL = {
    'listAPI':'/simple/list',
    'ArticleAPI':'/articles',
    'BigTagAPI':'/bigtag',
    'TagAPI':'/tags',
    'TagRelationAPI':'/tags_relation',
    'catListAPI':'/cat/list',
    'TagtoArticleAPI':'/tagtoarticle'
}

const indexData = {
    state: {
        flowResult: null,
        articleDetail:null,
        pageStatus:1,
        TagList:null,
        currentTag:null
            },
    mutations: {
        saveIndexData(state, data) {
            state.flowResult = data;
        },
        saveArticleData(state,data){
            state.articleDetail = data;
        },
        savePageStatus(state,data){
            state.pageStatus = data;
        },
        saveTagList(state,data){
            state.TagList = data;
        },
        saveCurrentTag(state,data){
            state.currentTag = data;
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
        setCatData({commit},bigtag_id){
            axios({
            url: `${API}${URL.catListAPI}/${bigtag_id}`,
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
        setTagList({commit}){
           axios({
            url: `${API}${URL.TagAPI}`,
            method: 'get',
            timeout: 10000
          })
            .then(function (res) {
                commit('saveTagList', res.data.con)
            })
            .catch(function(err){
            }) 
        },
        setTagtoArticleData({commit},tag_id){
            axios({
            url: `${API}${URL.TagtoArticleAPI}/${tag_id}`,
            method: 'get',
            timeout: 10000
          })
            .then(function (res) {
                commit('saveIndexData', res.data.con)
            })
            .catch(function(err){
            })
        },
        setCurrentTag({commit},tag_obj){
            commit('saveCurrentTag',tag_obj)
        },
        initArticleData({commit}) {
            commit('saveArticleData',null)
        },
        initListData({commit}){
            commit('saveIndexData',null)
        },
        initCurrentTag({commit}){
            commit('saveCurrentTag',null)
        },
        setPageStatus({commit},state_flag){
            commit('savePageStatus',state_flag)
        }   
    },
    getters:{
        getPageStatus: state => state.pageStatus,
        getCurrentTag: state => state.currentTag
    }
}

export default indexData