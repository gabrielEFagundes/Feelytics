import { createRouter, createWebHistory } from "vue-router";

import Home from '../pages/Home/Home.vue';
import PrivacyPol from "../pages/PrivacyPolicy/PrivacyPol.vue";
import Authentication from "../pages/Authentication/Auth.vue";
import TermsAndConditions from "../pages/Terms&Conditions/TermsAndConditions.vue";
import RedditDashboards from "../pages/Dashboards/RedditDashboards.vue";

const routes = [
    { path: '/', component: Home },
    { path: '/home', component: Home },
    { path: '/policy', component: PrivacyPol },
    { path: '/auth', component: Authentication, props: true },
    { path: '/terms', component: TermsAndConditions },
    { path: '/dashboards/reddit', component: RedditDashboards },
]

export const router = createRouter({
    history: createWebHistory(),
    routes
})