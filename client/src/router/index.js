import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import Athletes from '@/components/Athletes';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/athletes',
      name: 'Athletes',
      component: Athletes,
    },
  ],
  mode: 'history',
});
