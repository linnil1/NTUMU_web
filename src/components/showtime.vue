<template>
	<div id="showtime">	
		<link href='http://fonts.googleapis.com/css?family=Droid+Serif|Open+Sans:400,700' rel='stylesheet' type='text/css' async>
		<link rel="stylesheet" href="css/showtime.css"> <!-- Resource style -->
		<header>
			<h1>{{title}}</h1>
			<h2>地點: {{where}}</h2>
		</header>
	
		<section id="cd-timeline" class="cd-container">
			<div class="cd-timeline-block" v-for="show in shows">
				<div class="cd-timeline-img cd-picture">
					<img v-if="show.time!='pause'" v-bind:src="show.logo_src" alt="clublogo">
					<span v-else class="glyphicon glyphicon-pause"/>
				</div> <!-- cd-timeline-img -->
	
				<div class="cd-timeline-content">
					<h4>{{show.chinese}}</h4>
					<p v-if="show.title">{{show.title}}</p>
					<span class="cd-date">{{show.time}}</span>
				</div> <!-- cd-timeline-content -->
			</div> <!-- cd-timeline-block -->
		</section>
	</div>
</template>
		
<style scoped src="./showtime.css" />
<!-- <style scoped src='http://fonts.googleapis.com/css?family=Droid+Serif|Open+Sans:400,700' /> -->

<script>
export default {
	name: 'showtime',
	props: ['ver'],
	data(){ return {
		title: "",
		where: "",
		shows: []
	}},
	methods:{
	create: function(){
		$(".title-word").html("武聯-表演時間")

		var self = this.$data
		self.shows = []
		var jsondata = this.$store.state.clubsdata,
			ts = this.ver

		self.title = jsondata[ts].showtime.title 
		self.where = jsondata[ts].showtime.where
		jsondata[ts].showtime.shows.forEach( function(show){
			self.shows.push({
				name    : show.name,
				time    : show.time,
				title   : show.title,
			})
			var jdata = jsondata[show.name]
			if(jdata){
				self.shows[self.shows.length-1].chinese = jdata.chinese
				self.shows[self.shows.length-1].logo_src =  "./static/img/clublogo/"+jdata.logo
			}
			else
				self.shows[self.shows.length-1].chinese = show.name
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
