import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Athletes from '@/components/Athletes';
import Gantt from '@/components/Gantt';

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
    {
      path: '/gantt',
      name: 'Gantt',
      component: Gantt,
    },


  ],
  mode: 'history',
});
