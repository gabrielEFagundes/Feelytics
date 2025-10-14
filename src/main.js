import { createApp } from 'vue'
import './static/style.css'
import './static/tailwind.css'
import App from './pages/App.vue'
import { router } from './routes/router.js'

createApp(App).use(router).mount('#app')