import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import axios from "axios";

const apiClient = axios.post({
  baseURL: "/api/",
});

const app = createApp(App);
app.config.globalProperties.$axios = apiClient;
app.provide("api", apiClient);
app.use(router).use(store).use(vuetify);
app.mount("#app");

loadFonts();
