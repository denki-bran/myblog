import axios from 'axios'

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
            url: 'https://www.easy-mock.com/mock/5ba99867b9b3b431f78ef3e2/blog/index',
            method: 'get',
            timeout: 5000
          })
            .then(function (res) {
                commit('saveIndexData', res.data.data)
            })
            .catch(function (err) {
            })
        }
    }
}

export default indexData