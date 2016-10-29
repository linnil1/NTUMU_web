import Vue from 'vue'
/* eslint-disable no-new */

import App from './App'
import navbar from './navbar'
import foot from './foot'
import club from './components/club'

import 'bootstrap/dist/css/bootstrap.css'
var $ = require('jquery');
window.jQuery = $;
window.$ = $;

window.clubsdata = require('./assets/allclubs.json')
window.clubname = "TaiChi"
window.ts = "105_1"

new Vue({
  el: '#navbar',
  template: '<navbar/>',
  components: { navbar }
})

import VueRouter from 'vue-router'
Vue.use(VueRouter)

const router = new VueRouter({
	routes: [
    {
		path: '/',
		component: club,
    }
  ]
})

const app = new Vue({
	router,
	template:"<router-view></router-view>",
}).$mount('#app')
console.log(app)

new Vue({
  el: '#foot',
  template: '<foot/>',
  components: { foot }
})

