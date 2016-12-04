<template>
	<div class="container-fluid" id="countdown" style="background-color:#e9ebee">
		<!-- <script src="js/ekko-lightbox.js"></script> -->
		<div class="row">
			<div class="col-sm-10 col-sm-offset-1" style="padding:0">

				<!-- main object -->
				<div class="event-text">
					<h1>{{title}}</h1>
					<h3>{{desp }}</h3>
				</div>

				<!--slide show -->
				<!-- remove it beacuse it is not very well for look-->
				<!-- <div id="slideshow" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner" role="listbox" style="display:block">
						<div v-bind:class="['item',index==0 ? 'active' : '']" 
							 v-for="(count,index) in counts">
							<img class="img-responsive" v-bind:src="count.imgsrc" alt="" 
								 style="max-height:400px;margin:auto">
							<div class="carousel-caption">
								<h3>{{count.title}}</h3>
							</div>
						</div>
					</div>
					<a class="left carousel-control" role="button" data-slide="prev">
						<span class="glyphicon glyphicon-chevron-left" aria-hidden=""></span>
					</a>
					<a class="right carousel-control" role="button" data-slide="next">
						<span class="glyphicon glyphicon-chevron-right" aria-hidden=""></span>
					</a>
				</div> -->


				<!-- show all countdown desp -->
				<div v-for="(count,index) in counts">
					<div class="countdown-all">
						<div class="count-head">
							<h2>{{count.title}}</h2>
						<h4>{{count.chinese}}</h4>
					</div>
					<div class="count-body">
						<div class="count-img">
							<a v-bind:href="count.imgfullsrc"  data-toggle="lightbox">
								<img v-bind:src="count.imgsrc" class="img-responsive img-fluid">
							</a>
						</div>
						<div class="count-data">
							<p class="count-desp" v-html="count.desp"></p>
							<router-link v-bind:to="'/club/'+count.name" class="btn btn-default count-btn" href="#" role="button">詳細資訊</router-link>
						</div>
					</div>
				</div>
			</div>
		</div>
	 </div>
 </template>

<style scoped>
.count-head{
	text-align:center;
}



.countdown-all {
    -moz-border-bottom-colors: none;
    -moz-border-left-colors: none;
    -moz-border-right-colors: none;
    -moz-border-top-colors: none;
    border-color: #e5e6e9 #dfe0e4 #d0d1d5;
    border-image: none;
    border-radius: 3px;
    border-style: solid;
    border-width: 1px;
	background-color: #f6f7f9;
    color: #1d2129;
	margin: 10px;
}

.count-body{
	display: flex;
	justify-content:center;
	align-items:center;
	flex-wrap: wrap;
	position: relative;
}
.count-desp{
    word-wrap: break-word;
}

.count-data{
    margin: 20px;
    max-width: 400px;
    word-wrap: break-word;
}
.count-img{
	width:450px;
}

.count-img img{
	margin: 5px auto 15px auto;
	max-width: 100%;
	max-height: 400px;
}
.count-btn{
	float:right
}


@media only screen and (max-width : 768px) {
	.count-img{
		max-width:450px;
	}
	.countdown-all {
		margin:10px 3px;
	}
}
.event-text{
	text-align: center;
}
.carousel .carousel-control,
.carousel .carousel-caption { visibility: hidden; }
.carousel:hover .carousel-control,
.carousel:hover .carousel-caption{ visibility: visible; }
</style>

<script>

import lightbox from 'ekko-lightbox'
export default {
	name: 'countdown',
	data(){ return {
		title : "",
		desp  : "",
		counts : []
	}},
	created: function(){
		$(".title-word").html("武聯-倒數文案")

		var self = this.$data
		self.counts = []
		var jsondata = window.clubsdata,
			ts = window.ts,
			clubname = window.clubname

		self.title = jsondata[ts]['countdown']['title']
		self.desp  = jsondata[ts]['countdown']['desp']
		jsondata[ts]['countdown']['counts'].forEach( function(count){
			var jdata = jsondata[count.name]
			self.counts.push( {
				name : count.name,
				imgsrc : "./static/img/countdown/"+count.src,
				imgfullsrc : "./static/img/countdown/"+count.fullsrc,
				chinese : jdata.chinese,
				title  : count.title,
				desp   : count.desp
			})
		})

		//import lightbox from 'ekko-lightbox'
		$(document).delegate('*[data-toggle="lightbox"]','click', function(event) {
			event.preventDefault();
			$(this).ekkoLightbox();
		})
	},
	mounted:function(){
		window.scrollTo(0,0);// scroll to top when load
	},
	destroyed:function(){
		$(document).undelegate('*[data-toggle="lightbox"]','click')
	}
}

</script>
