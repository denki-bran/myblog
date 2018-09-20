const navBarStore = {
    state: {
        hoverSec:-1
    },
    mutations: {
        changeState(state,num){
            state.hoverSec = num;
        }
    },
    actions: {
        
    }
}

export default navBarStore