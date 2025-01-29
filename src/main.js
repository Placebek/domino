import './assets/base.css'

import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import { router } from './router/routers'

const app = createApp(App)
const pinia = createPinia()
// app.config.devtools = true
// app.config.productionTip = false
app.use(pinia)
app.use(router)
app.mount('#app')
// app.use(PrimeVue, {
//   theme: 'none',
// })
