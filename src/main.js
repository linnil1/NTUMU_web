import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App';
import Vuex from 'vuex';

Vue.use(VueRouter);
Vue.use(Vuex);

var data = require('./assets/allclubs.json');
var now = data.latest;

const store = new Vuex.Store({
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

const router = new VueRouter({
//  mode: 'history',
//  base: '/~b04611017',
  routes: [{
    path: '/',
    redirect: '/' + now + '/club' // why cannot ./105_1/
  }, {
    path: '/:ver(' + data.version.join('|') + ')',
    component: {'template': '<router-view></router-view>'},
    children: [ {
      path: 'club',
      props: true,
      component: require('./components/clublist.vue').default
    }, {
      path: 'club/:clubname',
      props: true,
      component: require('./components/club.vue').default
    }, {
      path: 'countdown',
      props: true,
      component: require('./components/countdown.vue').default
    }, {
      path: 'course',
      props: true,
      component: require('./components/course.vue').default
    }, {
      path: 'boothmap',
      props: true,
      component: require('./components/boothmap.vue').default
    }, {
      path: 'showtime',
      props: true,
      component: require('./components/showtime.vue').default
    }, {
      path: '*',
      redirect: 'club'
    }]
  }, {
    path: '*',
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

export default new Vue({
  router,
  store,
  template: '<app/>',
  components: {App}
}).$mount('#app');
