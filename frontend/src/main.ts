import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api/', // DjangoバックエンドのAPIエンドポイントのベースURLを指定
});

loadFonts();

createApp(App).use(router).use(store).use(vuetify).provide('api', apiClient).mount("#app");

