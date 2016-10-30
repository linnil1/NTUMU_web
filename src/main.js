import Vue from 'vue'
/* eslint-disable no-new */

import App from './App'
import club from './components/club'

import 'bootstrap/dist/css/bootstrap.css'
var $ = require('jquery');
window.jQuery = $;
window.$ = $;

window.clubsdata = require('./assets/allclubs.json')
window.clubname = "TaiChi"
window.ts = "105_1"

import VueRouter from 'vue-router'
Vue.use(VueRouter)

const router = new VueRouter({
	routes: [
    {
		path: '/club/:clubname',
		component: club,
		name: 'clublink',
		beforeEnter: function(to,from,next){
			console.log(to.params.clubname)
			window.clubname = to.params.clubname
			next();
		}
    }]
})

const app = new Vue({
	router,
	template: '<app/>',
	components:{App}
}).$mount('#app')
