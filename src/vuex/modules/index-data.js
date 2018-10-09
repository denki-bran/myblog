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
        flowResult: null
            },
    mutations: {
        saveIndexData(state, data) {
            state.flowResult = data;

        }
    },
    actions: {
        setIndexData({commit}) {
           axios({
            // url: 'https://www.easy-mock.com/mock/5ba99867b9b3b431f78ef3e2/blog/index',
            url: `${API}${URL.listAPI}`,
            method: 'get',
            timeout: 5000
          })
            .then(function (res) {
                commit('saveIndexData', res.data.con)
            })
            .catch(function (err) {
            })
        }
    }
}

export default indexData