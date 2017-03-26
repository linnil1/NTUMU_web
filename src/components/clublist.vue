<template>
	<div>
		<div class="container-fluid" id="card">
			<div class="row" style=" background-color: #eee;">
				<div class="col-sm-1"></div>
				<div class="col-sm-10 card-container">
					<router-link class="card-horizon" v-for="club in clubs" v-bind:to="'/'+ver+'/club/'+club.name" tag="div" :key="club">
							<div class="card-img">
								<img v-bind:src="club.logo_src" alt="club_logo">
							</div>
							<div class="card-text">
								<div class="card-title">
									{{club.chinese}}
								</div>
								<div class="card-subtitle">
									{{club.english}}
								</div>
							</div>
					</router-link>
				</div>
				<div class="col-sm-1"></div>
			</div>
		</div>
		<foot></foot>
	</div>
</template>

<style scoped>
.card-container{
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
	padding: 20px 0px 60px;
}
.card-horizon{
    box-shadow: 0 1px 1px 0 rgba(0,0,0,.2);
    height: 75px;
    width: 30%;
	overflow: hidden;
	margin: 1vw;
	background-color : white;
	display : flex;
}
.card-horizon:hover {
    box-shadow: 0 2px 8px 0 rgba(0,0,0,.25);
	cursor: pointer;
}
.card-img{
	background-color: #fafafa;
	height: 100%;
	width: 30%;
	display : flex;
	justify-content:center; /* veritcal align */
}
.card-img img{
	margin: auto;
	padding : 5px;
	max-width: 100%;
	max-height: 100%;
}
.card-text{
	width: 70%;
	right: 0;
	text-align: center;
	height: 100%;
	color: #222;
	display : flex;
	justify-content: center;
	flex-direction: column; 
}
.card-title{
	font-size : 1.2em;
}
.card-subtitle{
	font-size : 0.8em;
}
@media only screen and (max-width : 768px) {
	.card-horizon{
		width: 45%;
		margin: 0.5rem;
	}
}
@media only screen and (max-width : 480px) {
	.card-horizon{
		height: 200px;
		flex-direction: column;
		align-items: center;
	}
	.card-img{
		width: 100%;
		height: 65%;
	}
	.card-text{
		width: 100%;
		height: 35%;
	}
	.card-container{
		padding: 10px 0 40px 0;
	}
}
</style>

<script>

import foot from './../foot'
export default {
	name: 'clublist',
	props: ['ver'],
	data(){ return {
		clubs : []
	}},
	components: {
		foot
	},
	methods:{
	create: function(){
		$(".title-word").html("武聯-社團們")
		var self = this.$data
		var clubs = []
		var jsondata = this.$store.state.clubsdata,
			ts = this.ver
		jsondata[ts].clubs.forEach( function(clubname){
			var jdata = jsondata[clubname]
			clubs.push({
				chinese : jdata.chinese,
				name    : clubname,
				logo_src :  "./static/img/clublogo/"+jdata.logo,
				english : jdata.english
			})

			self.clubs = clubs
		})
		window.scrollTo(0,0);// scroll to top when load
	}},
	created: function(){ // not very well methods for reused component
		this.create()
	},
	watch: {
		'$route' (to, from) {
			this.create()
		}
	},
}
</script>
