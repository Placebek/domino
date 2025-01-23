import './assets/base.css'

import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import { router } from './router/routers'

const app = createApp(App)
app.use(createPinia())
app.use(router)
// app.use(PrimeVue, {
//   theme: 'none',
// })
app.mount('#app')
