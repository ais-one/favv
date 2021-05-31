// import { VERSION } from '/config.js'
import { createApp } from 'vue'
import router from './router.js'
import store from './store.js'
import { createPinia } from 'pinia'
import App from './App.vue'

import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import { formProps } from 'ant-design-vue/lib/form'
// import 'ant-design-vue/dist/antd.dark.css'

const app = createApp(App)
app.config.productionTip = false
app.use(store)
app.use(createPinia())
app.use(router)
app.use(Antd)

app.mount('#app')
