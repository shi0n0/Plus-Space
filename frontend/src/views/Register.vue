<template>
  <form @submit.prevent="registerUser">
    <label for="username">ユーザー名:</label>
    <input type="text" v-model="username" required />

    <label for="password">パスワード:</label>
    <input type="password" v-model="password" required />

    <button type="submit">登録</button>
  </form>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  data() {
    return {
      username: "",
      password: "",
    };
  },
  
  methods: {
    async registerUser() {
      try {
        // @ts-ignore
        const response = await axios.post("/api/register/", {
          username: this.username,
          password: this.password,
        });
        console.log(response.data); // 登録成功時のレスポンスを表示（任意）
      } catch (error: any) {
        console.error(error.response.data); // エラーレスポンスを表示（任意）
      }
    },
  },
});
</script>
