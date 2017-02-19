<template>
	<div class="container-fluid" style="padding-bottom:60px">
		<div class="row">
			<div class="col-sm-2">
				<div v-bind:style="sidebar_style" class="sidebar"  id="sidebar_id">
					<img class="img-responsive" v-if="logo_src" v-bind:src="logo_src" alt="club_logo"> 
					<h1> {{chinese}} </h1>
					<!-- <p> 版本
						<select v-model="ts">
							<router-link v-for="ver in version"
							             v-bind:to="'/'+ver+'/club/'+clubname" 
							             v-bind:value="ver"
							             tag="option">
								{{ver}}</router-link> 
						</select>
					</p> -->
					<ul>
						<li v-for="intro in main_intros">
							<router-link v-bind:to="('#'+intro.id)" v-bind:class="intro.id == activeid ? 'active' : ''" >{{intro.name}}</router-link>
						</li>
						<li>
							<router-link to="#connect">聯絡資訊</router-link>
						</li>
							
					</ul>
				</div>
			</div>

			<div class="col-sm-6">
				<!-- for phone -->
				<div class="smallscreen">
					<img class="img-responsive" v-bind:src="logo_src" alt="club_logo" > 
					<h1 > {{chinese}} </h1>
					<h2 > {{english}} </h2>
				</div>

				<div v-for="intro in main_intros" v-bind:id="intro.id">
					<h2>{{intro.name}}
						<router-link v-bind:to="('#'+intro.id)" class="glyphicon glyphicon-tags" style="font-size:15px"></router-link>
					</h2>
					<span v-if="intro.id=='qa'">
						<span v-for="qa in intro.content">
							<div class="question"> {{qa.q}} </div>
							<div class="answer">   {{qa.a}} </div>
						</span >
					</span>
					<div v-else v-html="intro.content" class="markdown-body"></div>
				</div>
			</div>

			<div class="col-sm-4">
				<div class="connect" id='connect' style="padding-left: 10px">
					<h2>聯絡資訊
						<router-link to="#connect" class="glyphicon glyphicon-tags" style="font-size:15px"></router-link>
					</h2>
					<h3>社長</h3>
					<p>{{info.president}}</p>
					<h3>Email</h3>
					<p>{{info.email}}</p>
					<h3 v-if="info.blog">部落格</h3>
					<p> <a v-bind:href="info.blog" target="_blank">{{info.blog}}</a> </p>
					<h3 v-if="info.fb">FB</h3>
					<p v-if="info.fb"> <a v-bind:href="info.fb.link" target="_blank">{{info.fb.name}}</a> </p>
					<h3>迎新</h3>
					<div v-for="wel in welcomes">
						<h4 v-if="wel.title"> {{wel.title}} </h4>
						<p> 時間: {{wel.time}} </p>
						<p> 地點: {{wel.place}} </p>
					</div>
					<h3>上課</h3>
					<div v-for="wel in courses">
						<h4 v-if="wel.title"> {{wel.title}} </h4>
						<p> 時間: {{wel.time}} </p>
						<p> 地點: {{wel.place}} </p>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style src="github-markdown-css"></style>
<style scoped>
#qa{
	overflow: auto;
}
#qa div{
	display: block;
	width: 70%;
	padding :5px 8px 4px;
	margin: 5px;
	border-radius: 12px;
}
.question{
	float:right;
	background-color: #4080ff;
	color: #fff;
	border-top-right-radius: 2px !important;
}
.answer{
	float:left;
	background-color: #f1f0f0;
	color: #4b4f56;
	border-top-left-radius: 2px !important;
	margin-bottom:15px !important;
}

.connect p{
	text-indent : 15px;
}
.connect h4{
	text-indent : 7px;
}
h2 a{
	padding-top:70px;
}

.smallscreen img{
	margin:10px auto;
	max-width:300px;
	max-width:100%;
	max-height:300px;
}
.smallscreen *{
	text-align:center;
	border-bottom: 0 !important;
}
</style>

<style scoped>  /* sidebar */
@media (min-width:768px ) {
	#sidebar_collapse{
		display: none;
	}
}
.active{
	color :#42b983 !important;
	font-size : 110%;
}
.sidebar{
	position: relative;
	padding-left: 10px;
	padding-right: 5px;
	padding-top: 20px;
	padding-bottom: 50px;
    bottom:0;
	overflow-y: scroll;
	overflow-x: hidden;
}
.sidebar img{
	padding-top:20px;
}
.sidebar ul{
	line-height: 1.8em;
    list-style-type: none;
	margin-left: 5px; 
	overflow-x: hidden; 
	overflow-y: auto; 
	padding: 0;
}
.sidebar ul li a{
	color : #34495e;
}
#sidebar_collapse_btn{
	float:left;
}
.sidebar *{
	text-align:center;
}
.sidebar h1{
	border-bottom: 0 !important;
	margin: 5px auto;
}
@media (min-width:768px ) {
	.smallscreen{
		display:none;
	}
}
@media (max-width:768px ) {
	.sidebar{
		margin: 0;
		top: 50px;
		left: 0;
		display: none;
		width: 100%;
		height: 100%;
		background-color : #f9f9f9;
		position: fixed;
		z-index : 5;
	}
	.sidebar img{
		float : right;
		max-height: 70%;
		max-width: 40%;
		padding: 10px;
		padding-right: 30px;
	}
}

</style>

<script>

export default {
	name: 'club',
	props: ['clubname','ver'],
	data(){ return {
		activeid : "",
		sidebar_style : {},
		info: {},
		chinese : "",
		english: "",
		courses : [],
		welcomes: [],
		ts: "",
		version : [],
		main_intros : [],
		logo_src : ""
	}},
	methods:{
		create : function(){
			// normal data
			console.log(this.clubname)
			console.log(this.ver)
			var data = this.$data
			var club = this.$store.state.clubsdata[this.clubname]
			var ts = data.ts = this.ver
			data.version = club.version
			if( club.version.indexOf(ts) == -1 ){
				console.log("error Page")
				return 
			}
			else
				club = club[ts]
			data.chinese = club.chinese
			data.english = club.english
			data.courses = club.course
			data.welcomes= club.welcome
			data.info    = club.info
			data.main_intros = jQuery.extend(true, {}, club.intro); //deep copy
			data.logo_src =  "./static/img/clublogo/"+club.logo
			$(".title-word").html(data.chinese)

			// sidebar
			this.$nextTick(function () {
				this.sidebar_style = { 
					position: "fixed" ,
					top : document.getElementById("navbar").offsetHeight+"px",
					width :$(".col-sm-2").width()+"px"
				}
				document.addEventListener('scroll',this.updatescroll)
			})

			// scroll to hash 
			var hash = this.$route.hash
			if(hash)
			{
				console.log("GO TO "+hash)
				this.$nextTick(function () {
					this.scrollToId(hash)
				})
			}
			else{
				window.scrollTo(0,0);// scroll to top when load
			}
		},
		updatescroll : function(){
			var scroll = document.documentElement.scrollTop || document.body.scrollTop
			// sidebar link active or not
			for(var i in this.main_intros){
				var intro = this.main_intros[i]
				if(intro.element == undefined)
					intro['element'] = document.getElementById(intro.id)
				if(intro.element.offsetTop+intro.element.offsetHeight > scroll ){
					this.activeid = intro.id;
					break;
				}
			}
		},
		scrollToId : function(hash){
			if(hash){ 
				$('html, body').animate({
					scrollTop: $(decodeURI(hash)).offset().top
				},1000);
			}
		}
	},
	created: function(){ // not very well methods for reused component
		this.create()
	},
	watch: {
		'$route' (to, from) {
			document.removeEventListener('scroll',this.updatescroll)
			this.create()
		}
	},
	destroyed: function(){
		document.removeEventListener('scroll',this.updatescroll)
	}
}
</script>
