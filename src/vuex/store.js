import Vue from 'vue'
import Vuex from 'vuex'
import navBarStore from './modules/navBar-store'
import indexData from './modules/index-data'

Vue.use(Vuex)

const store = new Vuex.Store({
    modules:{
        navBarStore,
        indexData
    }
})

export default store