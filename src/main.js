import Vue from 'vue'
/* eslint-disable no-new */

import App from './App'

window.clubsdata = require('./assets/allclubs.json')
window.clubname = "TaiChi"
window.ts = "105_1"

import VueRouter from 'vue-router'
Vue.use(VueRouter)

const router = new VueRouter({
//	mode: 'history',
	base: '/~b04611017',
	routes: [ {
		path: '/',
		redirect: "/club/"
    },{
		path: '/club',
		component: resolve => require(['./components/clublist.vue'], resolve)
    },{
		path: '/club/:clubname',
		component: resolve => require(['./components/club.vue'], resolve),
		beforeEnter: function(to,from,next){
			window.clubname = to.params.clubname
			next()
		}
    },{
		path: '/countdown',
		component: resolve => require(['./components/countdown.vue'], resolve)
    },{
		path: '/course',
		component: resolve => require(['./components/course.vue'], resolve)
    },{
		path: '/boothmap',
		component: resolve => require(['./components/boothmap.vue'], resolve)
    },{
		path: '/showtime',
		component: resolve => require(['./components/showtime.vue'], resolve)
    }]
})

const app = new Vue({
	router,
	template: '<app/>',
	components:{App}
}).$mount('#app')
