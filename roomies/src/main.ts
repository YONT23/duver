import { createApp } from 'vue'
import App from './App.vue'
import {router} from '../src/router/router';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import PrimeVue from 'primevue/config';
import Dialog from 'primevue/dialog';
import axios from 'axios'
import VueAxios from 'vue-axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app =
createApp(App)
app.use(router);
app.use(VueAxios, axios)
app.use(Antd);
app.use(PrimeVue);
app.component('Dialog', Dialog);
app.mount('#app')

