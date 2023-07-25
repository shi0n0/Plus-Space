import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/register',
    component: () => import('@/views/Register.vue'),
  },
  {
    path: '/login',
    component: () => import('@/views/Login.vue'),
  },
  {
    path: '/logout',
    component: () => import('@/views/Logout.vue'),
  },
  // その他のルートを追加する場合はここに記述
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
