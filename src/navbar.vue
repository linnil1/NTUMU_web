<template>
	<nav class="navbar navbar-default navbar-fixed-top" id="navbar">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-collapse" aria-expanded="false">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<router-link to="/" class="navbar-brand">
					<img src="static/img/105_1_logo.png"  height="50" alt="logo">
				</router-link>
				<a class="title-word navbar-brand navbar-word">台大武術聯盟</a>
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
							<option is="router-link" 
							        v-for="ver in versions"
							        :selected = "ver == ts"
							        :to  ="urlmodify(ver)" 
									tag="option">
									{{ver}}
							</option>
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
.navbar ul.grid li a{
	display:block;
	border:none;
}
.navbar-brand img{
	position: relative;
	top:-15px;
	left:-15px;
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
@media only screen and (max-width : 768px) {
	.navbar-word{
		display: inline-block;
		position: relative;
		left:-30px;
		padding:inherit 0 inherit 0;
		max-width: calc(100vw - 150px);/* logo 90+ button 45+ padding 30 */
		white-space: nowrap;
		overflow: hidden;
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
			var want = s.slice( s.indexOf('/',1)+1)

			// not good methods
			console.log(s)
			if( ['showtime','countdown','boothmap'].indexOf(want) >= 0 && 
				!( want in this.$store.state.clubsdata[v] ) )
				return '/'+v+"/club"
			return '/'+v+'/'+want
		}
	},
	computed: {
		ts: function(){
			return this.$store.state.ver
		},
		nav_bar: function(){
			var option = [ {
				name: '攤位',
				url: "/boothmap"
			},{
				name: '表演節目',
				url: "/showtime"
			},{
				name: '倒數',
				url: "/countdown"
			}]			
			var clubdata = this.$store.state.clubsdata,
				ts = this.$store.state.ver

			var new_var = option.filter( function(opt){
				return opt.url.slice(1) in clubdata[ts]} )
			new_var.push({ 
				name: '課表',
				url: "/course" 
			})
			return new_var
		}

	}

}
</script>

