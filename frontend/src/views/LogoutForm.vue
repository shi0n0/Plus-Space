<script lang="ts">
import { defineComponent, inject } from 'vue';
import axios from 'axios';

export default defineComponent({
  setup() {
    const api = inject<any>('api'); // Vuexストアを注入

    const logoutUser = async () => {
      try {
        // @ts-ignore
        const response = await axios.post('/api/logout/');
        console.log(response.data); // ログアウト成功時のレスポンスを表示（任意）
        api.setLoginState(false); // ログイン状態をVuexストアにセット
      } catch (error: any) {
        console.error(error.response.data); // エラーレスポンスを表示（任意）
      }
    };

    return {
      logoutUser,
    };
  },
});
</script>