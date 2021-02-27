import { createSSRApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router';
import { createStore } from 'vuex';

var data = require('./assets/allclubs.json');
var now = data.latest;

const store = createStore({
  state: {
    clubsdata: data,
    ver: now,
    title: '台大武術聯盟'
  },
  mutations: {
    verSet (state, ver) {
      state.ver = ver;
    },
    titleSet (state, title) {
      state.title = title;
      document.title = title;
    }
  }
});

const router = createRouter({
  history: createWebHistory(),
  routes: [{
    path: '/',
    redirect: '/' + now + '/club' // why cannot ./105_1/
  }, {
    path: '/:ver(' + data.version.join('|') + ')',
    component: {'template': '<router-view></router-view>'},
    children: [ {
      path: 'club',
      props: true,
      component: import('./components/clublist.vue'),
    }, {
      path: 'club/:clubname',
      props: true,
      component: import('./components/club.vue')
    }, {
      path: 'countdown',
      props: true,
      component: import('./components/countdown.vue')
    }, {
      path: 'course',
      props: true,
      component: import('./components/course.vue')
    }, {
      path: 'boothmap',
      props: true,
      component: import('./components/boothmap.vue')
    }, {
      path: 'showtime',
      props: true,
      component: import('./components/showtime.vue')
    }, {
      path: ':pathMatch(.*)',
      redirect: 'club'
    }]
  }, {
    path: '/:pathMatch(.*)',
    redirect: (route) => {
      return '/' + now + route.path;
    }
  }]
});

router.beforeEach(function (to, from, next) {
  // sync version
  if (!to.params.ver) {
    next();
    return;
  }
  store.commit('verSet', to.params.ver);
  console.log(store.state.ver);
  next();
});


import App from './App.vue';

const app = createSSRApp({
  // el: "#app",
  // store,
  // router,
  template: '<app/>',
  components: {App},
  // render: h => h(App),
});
app.use(store);
app.use(router);
app.mount('#app');

export default app;
