<template>
	<div>
		<!-- use div beacuse it can't not use template -->
		<navbar></navbar>
		<router-view></router-view>
	</div>
</template>


<script>
	import navbar from './navbar'
	
	export default {
		name: 'app',
		components: {
			navbar
		}
	}
</script>
