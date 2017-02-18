import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
import Vuex from 'vuex'
Vue.use(Vuex)

var now = "105_1"
var versions = ["105_1"] // should be sorted
const store = new Vuex.Store({
	state: {
		clubsdata  : require('./assets/allclubs.json'),
		'versions' : versions,
		ver        : now
	},
	mutations: {
		verSet (state, ver) {
			state.ver = ver
		}
	}
})

const router = new VueRouter({
//	mode: 'history',
	base: '/~b04611017',
	routes: [ {
		path: '/',
		redirect: '/'+now+'/club' //why cannot ./105_1/
    },{
		path: '/:ver('+versions.join('|')+')',
		component: {'template':'<router-view></router-view>'},
		children:[ {
			path: 'club',
			props: true,
			component: resolve => require(['./components/clublist.vue'], resolve)
		},{
			path: 'club/:clubname',
			props: true,
			component: resolve => require(['./components/club.vue'], resolve)
		},{
			path: 'countdown',
			props: true,
			component: resolve => require(['./components/countdown.vue'], resolve)
		},{
			path: 'course',
			props: true,
			component: resolve => require(['./components/course.vue'], resolve)
		},{
			path: 'boothmap',
			props: true,
			component: resolve => require(['./components/boothmap.vue'], resolve)
		},{
			path: 'showtime',
			props: true,
			component: resolve => require(['./components/showtime.vue'], resolve)
		},{
			path: '*',
			redirect: "club"
		}]
    },{
		path: '*',
		redirect: (route)=>{
			return '/'+now+route.path}
	}]
})

router.beforeEach( function(to, from, next){
	// sync version
	if(!to.params.ver){
		next()
		return 
	}
	store.commit("verSet",to.params.ver)
	console.log(store.state.ver)
	next()
})

import App from './App'
const app = new Vue({
	router,
	store,
	template: '<app/>',
	components:{App}
}).$mount('#app')
