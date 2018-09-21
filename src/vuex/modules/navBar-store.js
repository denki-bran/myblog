const navBarStore = {
    state: {
        hoverSec:3
            },
    mutations: {
        changeState(state,num){
            state.hoverSec = num;
        }
    },
    actions: {
        setChangeState({commit},{num}){
            commit('changeState',num);
        }
    }
}

export default navBarStore