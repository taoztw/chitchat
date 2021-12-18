import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import panel from "../components/panel";
Vue.use(Router)

export default new Router({
    mode:'history',
    routes: [
        {path:"/",component: panel},
        {path:"/login",component: Login},
    ]
})
