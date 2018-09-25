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
    }
  ]
})
