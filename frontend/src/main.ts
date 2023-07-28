import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import axios from "axios";

// @ts-ignore
const apiClient = axios.create({
  baseURL: "/api/", // DjangoバックエンドのAPIエンドポイントのベースURLを指定
});

const app = createApp(App);
app.config.globalProperties.axios = apiClient; // axiosをVueインスタンスのプロパティとして追加
app.use(router).use(store).use(vuetify);
app.provide("api", apiClient); // APIクライアントをprovide

app.mount("#app");

loadFonts();
