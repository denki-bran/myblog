import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import Article from '@/views/Article.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/article/:article_id',
      name: 'article',
      component:Article
    },
    {
      path:'/cat/:cat_name',
      name:'cat',
      component:Home
    },
    {
      path:'/taglist',
      name:'taglist',
      component:Home
    },
    {
      path:'/tag/:tag_id',
      name:'tag',
      component:Home
    }
  ]
})
