import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore } from '../stores/auth.store'
import { Login, Home, VideoC, HomeDetail } from '../components/pages'

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  routes: [
    { path: '/', component: Home },
    { path: '/video', component: VideoC },
    { path: '/login', component: Login },
    { path: '/:id', component: HomeDetail },
  ],
})

router.beforeEach(async (to) => {
  const publicPages = ['/login']
  const authRequired = !publicPages.includes(to.path)
  const auth = useAuthStore()

  //   if (authRequired && !auth.user) {
  //     auth.returnUrl = to.fullPath
  //     return '/login'
  //   }
})
