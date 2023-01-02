import { createRouter, createWebHistory } from 'vue-router'
import CookinHubHome from "@/views/HomeVue.vue";
import CookinHubNav from "@/views/ReceipeVue.vue";
import CookinHubCustomize from "@/views/CustomizeVue.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: CookinHubHome
  },
  {
    path: '/receipe/:receipe',
    name: 'receipe',
    component : CookinHubNav,
    props: true
  },
  {
    path: '/customize',
    name: 'customize',
    component : CookinHubCustomize
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
