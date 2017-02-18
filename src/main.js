import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
import Vuex from 'vuex'
Vue.use(Vuex)

var data = require('./assets/allclubs.json')
var now = data.latest

const store = new Vuex.Store({
	state: {
		clubsdata  : data,
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
		path: '/:ver('+data.version.join('|')+')',
		component: {'template':'<router-view></router-view>'},
		children:[ {
			path: 'club',
			props: true,
			component: require('./components/clublist.vue')
		},{
			path: 'club/:clubname',
			props: true,
			component: require('./components/club.vue')
		},{
			path: 'countdown',
			props: true,
			component: require('./components/countdown.vue')
		},{
			path: 'course',
			props: true,
			component: require('./components/course.vue')
		},{
			path: 'boothmap',
			props: true,
			component: require('./components/boothmap.vue')
		},{
			path: 'showtime',
			props: true,
			component: require('./components/showtime.vue')
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
