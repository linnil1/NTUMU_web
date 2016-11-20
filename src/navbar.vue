<template>
	<nav class="navbar navbar-default navbar-fixed-top" id="navbar">
		<div class="container-fluid">
			<div class="navbar-header">
				<button id="sidebar_collapse_btn" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar_id" v-if="clubhtml">導覽</button>
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
					<li v-for="nav in nav_bar">
						<router-link v-bind:to="nav.url">{{nav.name}}</router-link>
					</li>
					<li class="dropdown">
						<router-link class="dropdown-toggle" to="/club">{{club}}<b class="caret"></b></router-link>
						<ul class="dropdown-menu grid">
							<li v-for="club in clubs">
								<router-link v-bind:to="club.url">{{club.name}}</router-link>
							</li>
						</ul>
					</li>
				</ul>
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
	data(){ return {
		club : '社團',
		clubs: [],
		clubhtml: false,
		navbar_fix: "",
		search: 1, // never match 1
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
	created:function(){ // readjson
//		$(".title-word").html(this.title)
		var ts = window.ts,jsondata = window.clubsdata
		var clubs = this.clubs
		jsondata[ts].clubs.forEach(function(club){
			clubs.push({
				name: jsondata[club].chinese,
				url : '/club/'+club
			})
		})

		// navbar won't collapse after click
		$(document).on('click','.navbar-collapse.in',function(e) {
			if( $(e.target).is('a')){
				$(this).collapse('hide');
			}
		});
		$("body").css("padding-top","50px")
	},
}
</script>

