import { defineStore } from 'pinia'
import { router } from '../router/routers'
import axios from 'axios'

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    // initialize state from local storage to enable user to stay logged in
    user: JSON.parse(localStorage.getItem('user')),
    returnUrl: null,
  }),
  actions: {
    async login(phone_number, password) {
      const request = {
        phone_number: phone_number,
        password: password,
      }
      try {
        const response = await axios.post(`https://py-storm.space/auth/login`, request, {
          ContentType: 'application/json',
        })

        const user = response.data

        // update pinia state
        this.user = user

        // store user details and jwt in local storage to keep user logged in between page refreshes
        localStorage.setItem('user', JSON.stringify(user.access_token))

        // redirect to previous url or default to home page
        router.push(this.returnUrl || '/')
      } catch (error) {
        console.error('Login failed:', error)
        // здесь можно добавить обработку ошибок, например, вывод уведомления
        throw error
      }
    },
    async register(phone_number, password, first_name, last_name, email) {
      try {
        const request = {
          phone_number: phone_number,
          password: password,
          firstname: first_name,
          lastname: last_name,
          email: email,
        }
        debugger
        const response = await axios.post(`https://py-storm.space/auth/register`, request, {
          ContentType: 'application/json',
        })

        const user = response.data

        // update pinia state
        this.user = user
        debugger
        // store user details and jwt in local storage to keep user logged in between page refreshes
        localStorage.setItem('user', JSON.stringify(user.access_token))
        // redirect to previous url or default to home page
        router.push(this.returnUrl || '/')
      } catch (error) {
        console.error('Register failed:', error)
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
