import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Athletes from '@/components/Athletes';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Athletes',
      component: Athletes,
    },
  ],
  mode: 'history',
});
