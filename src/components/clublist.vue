<template>
	<div class="container-fluid" id="card">
		<div class="row" style=" background-color: #eee;">
			<div class="col-sm-1"></div>
			<div class="col-sm-10">
				<router-link class="card-horizon" v-for="club in clubs" v-bind:to="'/'+ver+'/club/'+club.name" tag="div">
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
</template>

<style scoped>
.card-horizon{
    box-shadow: 0 1px 1px 0 rgba(0,0,0,.2);
	float : left;
    height: 75px;
    width: 30%;
    position: relative;
	overflow: hidden;
	margin: 10px;
	background-color : white;
	display : flex;
	flex-direction: row
}
.card-horizon:hover {
    box-shadow: 0 2px 8px 0 rgba(0,0,0,.25);
}
.card-img{
	background-color: #fafafa;
	height: 100%;
	width: 25%;
	display : flex;
	justify-content:center;
}
.card-img img{
	margin: auto;
	padding : 5px;
	max-width: 100%;
	max-height: 100%;
}
.card-text{
	width: 75%;
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
		width: 40%;
	}
}
</style>

<script>

export default {
	name: 'clublist',
	props: ['ver'],
	data(){ return {
		clubs : []
	}},
	methods:{
	create: function(){
		$(".title-word").html("武聯-一覽")
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
	}},
	created: function(){ // not very well methods for reused component
		this.create()
	},
	watch: {
		'$route' (to, from) {
			this.create()
		}
	},
	mounted:function(){
		window.scrollTo(0,0);// scroll to top when load
	}
}
</script>
