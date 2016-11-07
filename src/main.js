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
		redirect: {name: 'clublist'}
    },{
		path: '/club',
		name: 'clublist',
		component: require('./components/clublist.vue')
    },{
		path: '/club/:clubname',
		component: require('./components/club.vue'),
		beforeEnter: function(to,from,next){
			window.clubname = to.params.clubname
			next()
		}
    },{
		path: '/countdown',
		component: require('./components/countdown.vue')
    },{
		path: '/course',
		component: require('./components/course.vue')
    },{
		path: '/boothmap',
		component: require('./components/boothmap.vue')
    },{
		path: '/showtime',
		component: require('./components/showtime.vue')
    }]
})

const app = new Vue({
	router,
	template: '<app/>',
	components:{App}
}).$mount('#app')
