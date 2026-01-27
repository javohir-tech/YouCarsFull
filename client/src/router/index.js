import { createRouter, createWebHistory } from 'vue-router'
///////////// MAIN LAYUOT ////////////
import mainLayout from '@/layout/mainLayout.vue'
///////////////// VIEWS ////////////////
import { Home } from '@/views'
import { singup } from '@/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: mainLayout,
      children: [
        ////// AUTH /////
        {
          path: "singup",
          component: singup
        },
        {
          path: "",
          component: Home
        },
      ]
    }
  ],
})

export default router
