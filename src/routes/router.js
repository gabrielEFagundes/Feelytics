import { createRouter, createWebHistory } from "vue-router";

import Home from '../pages/Home/Home.vue';
import PrivacyPol from "../pages/PrivacyPolicy/PrivacyPol.vue";

const routes = [
    { path: '/', component: Home },
    { path: '/home', component: Home },
    { path: '/policy', component: PrivacyPol }
]

export const router = createRouter({
    history: createWebHistory(),
    routes
})