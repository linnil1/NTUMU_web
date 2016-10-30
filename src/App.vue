<template>
	<container>
		<navbar></navbar>
		<router-view></router-view>
		<foot></foot>
	</container>
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
