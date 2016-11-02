<template>
	<div>
		<!-- use div beacuse it can't not use template -->
		<navbar></navbar>
		<router-view></router-view>
		<foot></foot>
	</div>
</template>


<script>
	import navbar from './navbar'
	import foot from './foot'
	
	export default {
		name: 'app',
		components: {
			navbar,foot
		}
	}
</script>
