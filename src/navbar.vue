<template>
	<container>
		<div id="LOGO" class="logo">
			<img src="./../static/img/permanent_logo.png" height="100" alt="LOGO">
			<h1>台大武術聯盟      </h1> 
			<h2>NTU Martial Union </h2>			
		</div>
		<nav class="navbar navbar-default" id="navbar" v-bind:class="navbar_fix">
				<div class="container-fluid">
					<div class="navbar-header">
						<button id="sidebar_collapse_btn" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar_id" v-if="clubhtml">導覽</button>
						<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-collapse" aria-expanded="false">
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<a href="#">
							<img src="static/img/105_1_logo.png"  height="50" alt="logo">
						</a>
						<h3 class="navbar-text mobile-hide title-word">title</h3>
					</div>
					<div class="collapse navbar-collapse" id="nav-collapse">
						<ul class="nav navbar-nav"  >
							<li v-for="nav in nav_bar">
								<a href="#">{{nav.name}}</a>
							</li>
							<li class="dropdown">
								<a href="#" class="dropdown-toggle">
									{{club}}<b class="caret"></b>
								</a>
								<ul class="dropdown-menu grid">
									<li v-for="club in clubs">
										<a href="#" >{{club.name}}</a>
									</li>
									<!-- <li class="divider"></li>-->
								</ul>
							</li>
						</ul>
					</div>
				</div>
			</nav>
	</container>
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
			url: "boothmap"
		},{
			name: '表演節目',
			url: "showtime"
		},{
			name: '倒數',
			url: "countdown"
		},{ 
			name: '課表',
			url: "course" 
		}],
	}},
	created:function(){ // readjson
		var ts = window.ts,jsondata = window.clubsdata
		var clubs = this.clubs
		jsondata[ts].clubs.forEach(function(club){
			clubs.push({
				name: jsondata[club].chinese,
				url : club
			})
		})
		$(".title-word").html(this.title)

	},
	methods:{
		navbarUpdate : function(){
			var scroll = document.documentElement.scrollTop || document.body.scrollTop
			var navbar_top = document.getElementById("LOGO").offsetHeight
			this.navbar_fix= scroll >= navbar_top ? "navbar-fixed-top" : ""

			$("body").css("padding-top",scroll >= navbar_top ? "70px":"0")
		}
	},
	mounted: function(){
		document.addEventListener('scroll',this.navbarUpdate)
		setInterval( this.urlUpdate , 500)
	},
	destroyed: function(){
		document.removeEventListener('scroll',this.navbarUpdate)
	}
}
</script>

