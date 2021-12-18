// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// 导入element-ui 以及样式
import ElementUI from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"

// 导入全局演样式
import "../static/css/global.css"

import settings from "./settings";

Vue.prototype.$settings = settings;

// 配置axios
import axios from "axios"
// 将axios注入到vue实例
Vue.prototype.$axios = axios



// 全局注册
Vue.use(ElementUI)



Vue.config.productionTip = false

import store from "./store/index"

/* eslint-disable no-new */


// 定义外部接口可配置
let startApp = function () {
    axios.get('/static/config.json').then((res) => {
        // 基础地址
        console.log(res)
        Vue.prototype.BASE_URL = res.data['BASE_URL'];

        new Vue({
            el: '#app',
            router,
            store,
            components: {
                App
            },
            template: '<App/>'
        })
    })
}

startApp()
