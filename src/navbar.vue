<template>
	<nav class="navbar navbar-default navbar-fixed-top" id="navbar">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-collapse" aria-expanded="false">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<router-link to="/">
					<img src="static/img/105_1_logo.png"  height="50" alt="logo">
				</router-link>
				<h3 class="title-word navbar-text mobile-hide">台大武術聯盟</h3>
			</div>
			<div class="collapse navbar-collapse" id="nav-collapse">
				<ul class="nav navbar-nav"  >
					<!-- Narbar -->
					<li v-for="nav in nav_bar">
						<router-link :to="'/'+ts+nav.url"
							>{{nav.name}}</router-link>
					</li>
					<!-- Club -->
					<li class="dropdown">
						<router-link class="dropdown-toggle" 
						             :to="'/'+ts+'/club'">
							{{club}}<b class="caret"></b></router-link>
						<ul class="dropdown-menu grid">
							<li v-for="club in clubs">
								<router-link v-bind:to="'/'+ts+club.url">{{club.name}}</router-link>
							</li>
						</ul>
					</li>
				</ul>

				<!-- Version -->
				<form class="navbar-form navbar-right">
					<div class="form-group">
						<span> {{versionname}} </span>
						<select>
							<!-- cannot use :key = "$route.path" -->
							<router-link v-for="ver in versions"
						                 :to  ="urlmodify(ver)"
										 :selected = "ver == ts"
							             tag  ="option">
								{{ver}}</router-link>
						</select>
					</div>
				</form>
			</div>
		</div>
	</nav>
</template>

<style scoped>
.navbar{
	margin: 0;
}
.navbar ul.grid{
	width: 570px;
}
.navbar ul.grid li{
	padding: 2px ;
	float:left;
}
.navbar-text {
	display: inline-block;
	margin: 0;
}
.navbar ul.grid li a{
	display:block;
	border:none;
}
@media only screen and (min-width : 768px) {
    /* Make Navigation Toggle on Desktop Hover */
    .dropdown:hover .dropdown-menu {
        display: block;
    }
	.mobile-hide{
		display: none;
	}
}
</style>

<script>

export default {
	name: 'navbar',
//	props: ['ver'],
	data(){ return {
		club : '社團',
		clubs: [],
		versionname : '版本',
		versions : [],
		title: "台大武術聯盟",
		
		nav_bar : [{
			name: '攤位',
			url: "/boothmap"
		},{
			name: '表演節目',
			url: "/showtime"
		},{
			name: '倒數',
			url: "/countdown"
		},{ 
			name: '課表',
			url: "/course" 
		}],
	}},
	created:function(){
//		$(".title-word").html(this.title)
		var jsondata = this.$store.state.clubsdata,
			ts = this.ts
		this.versions = jsondata.version
		var clubs = this.clubs
		jsondata[ts].clubs.forEach(function(club){
			clubs.push({
				name: jsondata[club].chinese,
				url : '/club/'+club
			})
		})

		// navbar collapse after click
		$(document).on('click','.navbar-collapse.in',function(e) {
			if( $(e.target).is('a')){
				$(this).collapse('hide');
			}
		});
		$("body").css("padding-top","50px")
	},
	methods:{
		// bad methods to modify version
		urlmodify: function(v){ 
			var s = this.$route.path
			return '/'+v+s.slice( s.indexOf('/',1))
		}
	},
	computed: {
		ts: function(){
			return this.$store.state.ver
		}
	}

}
</script>

