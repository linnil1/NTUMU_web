import Vue from 'vue'
import App from './App'
import navbar from './navbar'
import 'bootstrap/dist/css/bootstrap.css'

var $ = require('jquery');
window.jQuery = $;
window.$ = $;

/* eslint-disable no-new */
new Vue({
  el: '#navbar',
  template: '<navbar/>',
  components: { navbar }
})
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})

