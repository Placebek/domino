import { defineStore } from 'pinia'
import { router } from '../router/routers'
import axios from 'axios'

const baseUrl = `${import.meta.env.VITE_API_URL}/auth/admin/login`

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    // initialize state from local storage to enable user to stay logged in
    user: JSON.parse(localStorage.getItem('user')),
    returnUrl: null,
  }),
  actions: {
    async login(phone_number, password) {
      try {
        const response = await axios.post(
          baseUrl,
          { phone_number, password },
          { referrerPolicy: 'unsafe-url' }, // при необходимости можно убрать
        )

        const user = response.data

        // update pinia state
        this.user = user

        // store user details and jwt in local storage to keep user logged in between page refreshes
        localStorage.setItem('user', JSON.stringify(user))

        // redirect to previous url or default to home page
        router.push(this.returnUrl || '/')
      } catch (error) {
        console.error('Login failed:', error)
        // здесь можно добавить обработку ошибок, например, вывод уведомления
        throw error
      }
    },
    logout() {
      this.user = null
      localStorage.removeItem('user')
      router.push('/login')
    },
  },
})
