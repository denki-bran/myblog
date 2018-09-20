import Vue from 'vue'
import Vuex from 'vuex'
import navBarStore from './modules/navBar-store'

Vue.use(Vuex)

const store = new Vuex.Store({
    modules:{
        navBarStore
    }
})

export default store