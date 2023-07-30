<script lang="ts">
import { defineComponent, ref, inject } from 'vue';
import axios from 'axios';

export default defineComponent({
  setup() {
    const api = inject<any>('api'); // Vuexストアを注入
    const username = ref('');
    const password = ref('');

    const loginUser = async () => {
      try {
        // @ts-ignore
        const response = await axios.post('/api/login/', {
          username: username.value,
          password: password.value,
        });
        console.log(response.data); // ログイン成功時のレスポンスを表示（任意）
        api.setLoginState(true); // ログイン状態をVuexストアにセット
      } catch (error: any) {
        console.error(error.response.data); // エラーレスポンスを表示（任意）
      }
    };

    return {
      username,
      password,
      loginUser,
    };
  },
});
</script>
