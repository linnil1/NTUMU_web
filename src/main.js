import Vue from 'vue'
/* eslint-disable no-new */

import App from './App'
import club from './components/club'
import countdown from './components/countdown'

import bootstrap from 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'

window.clubsdata = require('./assets/allclubs.json')
window.clubname = "TaiChi"
window.ts = "105_1"

import VueRouter from 'vue-router'
Vue.use(VueRouter)

const router = new VueRouter({
	routes: [ {
		path: '/club/:clubname',
		component: club,
		beforeEnter: function(to,from,next){
			console.log(to)
			console.log(from)
			window.clubname = to.params.clubname
			next()
			console.log(next)
		}
    },{
		path: '/countdown',
		component: countdown
    }
	]
})

const app = new Vue({
	router,
	template: '<app/>',
	components:{App}
}).$mount('#app')
