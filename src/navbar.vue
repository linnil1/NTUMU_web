<template>
	<nav class="navbar navbar-default" id="navbar" v-bind:class="navbar_fix">
			<div class="container-fluid">
				<div class="navbar-header">
					<button id="sidebar_collapse_btn" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar_id" v-if="clubhtml">導覽</button>
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-collapse" aria-expanded="false">
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a href="#" v-on:click.prevent="urlGo('')">
						<img src="static/img/105_1_logo.png"  height="50" alt="logo">
					</a>
					<h3 class="navbar-text mobile-hide title-word">title</h3>
				</div>
				<div class="collapse navbar-collapse" id="nav-collapse">
					<ul class="nav navbar-nav"  >
						<li v-for="nav in nav_bar">
							<a href="#" v-on:click.prevent="urlGo(nav.url)">{{nav.name}}</a>
						</li>
						<li class="dropdown">
							<a href="#" v-on:click.prevent="urlGo('app=card')" class="dropdown-toggle">
								{{club}}<b class="caret"></b>
							</a>
							<ul class="dropdown-menu grid">
								<li v-for="club in clubs">
									<a href="#" v-on:click.prevent="urlGo(club.url)">{{club.name}}</a>
								</li>
								<!-- <li class="divider"></li>-->
							</ul>
						</li>
					</ul>
				</div>
			</div>
		</nav>
</template>

<style>
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

.footer {
	margin-top : 200px;
    background-color:  #5f5f5f;
    bottom: 0;
    width: 100%;
}
.footer *{
	text-align: center;
	color: white !important;
}

</style>

<script>

var jsondata = require('./assets/allclubs.json'),
	clubname = "",
	ts = "105_1"

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
			url: "app=boothmap"
		},{
			name: '表演節目',
			url: "app=showtime"
		},{
			name: '倒數',
			url: "app=countdown"
		},{ 
			name: '課表',
			url: "app=course" 
		}],
	}},
	created:function(){ // readjson
		console.log(jsondata)
		var clubs = this.clubs
		jsondata[ts].clubs.forEach(function(club){
			clubs.push({
				name: jsondata[club].chinese,
				url : club
			})
		})
		$(".title-word").html(this.title)
	}
}
</script>

