import axios from "axios";
import { SET_USER_TOKEN_DATA_MUTATION } from "./storeconstants";

const state = () => ({
  loginState: "",
  user_id: "",
  customer_id: "",
  refresh: "",
  access: "",
});

const getters = {
  getLoginState: (state) => state.loginState,
};

const actions = {
  async actionLogin(context, payload, config) {
    const response = await axios

      .post("/login/", payload, config, {
        withCredentials: true,
        credentials: "include",
      })

      .catch((err) => {
        console.log(err);
      });

    if (response && response.data) {
      console.log(response.data);
      localStorage.setItem("isAuthenticated", "true");
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("customer_id", response.data.customer);
      localStorage.setItem("refresh", response.data.refresh);
      localStorage.setItem("user_id", response.data.user);

      context.commit(SET_USER_TOKEN_DATA_MUTATION, {
        user_id: response.data.user,
        customer_id: response.data.customer,
        refresh: response.data.refresh,
        access: response.data.access,
      });

      context.commit("setLoginState", "success");
    } else {
      context.commit("setLoginState", "failed");
    }
  },
};

const mutations = {
  setLoginState(state, data) {
    state.loginState = data;
    state.access = localStorage.getItem("access_token");
  },

  [SET_USER_TOKEN_DATA_MUTATION](state, payload) {
    state.user_id = payload.user_id;
    state.customer_id = payload.customer_id;
    state.refresh = payload.refresh;
    state.access = payload.access;
  },
  initializeStore(state) {
    if (localStorage.getItem("access_token")) {
      state.access = localStorage.getItem("access_token");
      state.customer_id = localStorage.getItem("customer_id");
      state.user_id = localStorage.getItem("user_id");
      state.refresh = localStorage.getItem("refresh");
      state.loginState = true;
    } else {
      state.access = "";
      state.loginState = false;
    }
  },
};

// };

export default {
  namespaced: true,

  state,

  getters,

  actions,

  mutations,
};
