<template>
	<div id="LOGO" class="logo">
		<img src="static/img/permanent_logo.png" height="100" alt="LOGO">
		<h1>台大武術聯盟      </h1> 
		<h2>NTU Martial Union </h2>			
	</div>
</template>

<style scoped>
.logo{
	overflow: hidden;
	max-height: 100px;
}
.logo img{
	padding: 10px;
}
.logo h1,.logo h2{
	display: inline-block;
    vertical-align: bottom;
}
</style>

export default {
	name: 'logo'
}
