<template>
	<div class="container-fluid" id="countdown">
		<!-- <script src="js/ekko-lightbox.js"></script> -->
		<div class="row" style=" background-color: #eee;">
			<div class="col-sm-1"></div>
			<div class="col-sm-10">

				<!-- main object -->
				<div class="event-text">
					<h1>{{title}}</h1>
					<h3>{{desp }}</h3>
				</div>

				<!--slide show -->
				<!-- remove it beacuse it cannot use on it -->
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
						<img class="img-responsive" v-bind:src="count.imgsrc">
						<p class="count-desp" v-html="count.desp"></p>
						<router-link v-bind:to="'/club/'+count.name" class="btn btn-default" href="#" role="button">詳細資訊</router-link>
					</div>
				</div>
						<!-- <div class="media-left countdown-img" v-bind:class="index%2?'pull-left':'pull-right'">
							<a v-bind:href="count.imgfullsrc" v-bind:data-title="count.title+ '-'+ count.chinese" data-toggle="lightbox">
								<img class="media-object countdown-img" v-bind:src="count.imgsrc" alt="countdown_picture">
							</a>
						</div> -->
			</div>
		</div>
	 </div>
 </template>

<style scoped>
#countdown{
	width: 100%;
	margin:auto;
}
.count-head{
	text-align:center;
}

.countdown-all {
	position: relative;
	margin:100px auto;
	box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
	transition: 0.3s;
	padding: 10px;
}

.count-body{
	display: flex;
	justify-content:center;
	align-items:center;
	flex-wrap: wrap;
	position: relative;
}
.count-desp{
    margin: 20px 30px;
    max-width: 400px;
    width:100%;

    word-wrap: break-word;
}

.count-img{
	width:450px;
	text-align:center;
}

.count-body img{
	max-width: 450px;
	max-height: 400px;
}


@media only screen and (max-width : 768px) {
	.count-desp{
	}

	.count-body img{
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

<style src="./ekko-lightbox.css" scoped></style>
<script>
export default {
	name: 'countdown',
	data(){ return {
		counts : []
	}},
	created: function(){
		var self = this.$data
		self.counts = []
		var jsondata = window.clubsdata,
			ts = window.ts,
			clubname = window.clubname

		jsondata[ts]['countdown'].forEach( function(count){
			if(self.counts.length == 4) // unfinished
				return 0;
			var jdata = jsondata[count.name]
			self.counts.push( {
				name : count.name,
				imgsrc : "./../static/img/countdown/"+count.src,
				imgfullsrc : "./../static/img/countdown/"+count.fullsrc,
				chinese : jdata.chinese,
				title  : count.title,
				desp   : count.desp
			})
		})

		$(document).delegate('*[data-toggle="lightbox"]','click', function(event) {
			event.preventDefault();
			$(this).ekkoLightbox();
		})
		$(".title-word").html("武聯-倒數文案")
	}
}

</script>
