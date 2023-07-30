import { createStore } from 'vuex';

export default createStore({
  state: {
    isLoggedIn: false, // ログイン状態を管理するステート
  },
  mutations: {
    SET_LOGIN_STATE(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn;
    },
  },
  actions: {
    setLoginState({ commit }, isLoggedIn) {
      commit('SET_LOGIN_STATE', isLoggedIn);
    },
  },
});
