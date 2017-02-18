<template>
	<div id="boothmap">
		<div id="gmap"></div>
	</div>
</template>

<style scoped>
#boothmap{
	height: calc(100vh - 50px);
	width: 100%;
	margin: auto;
}
#gmap {
	height: 100%;
}
#gmap p,#gmap h3{
	padding: 5px;
	margin: 0;
}
</style>

<script>
var GoogleMapsLoader = require('google-maps');

export default {
	name: 'boothmap',
	props: ['ver'],
	data(){ return {
		map:null,
		lastopen:null
	}},
	methods:{
	create: function(){
		$(".title-word").html("武聯-攤位地圖")
		var self = this.$data;
		var jsondata = this.$store.state.clubsdata,
			ts = this.ver,
			boothmap = jsondata[ts]['boothmap']
		var build = this.mapBuild
		GoogleMapsLoader.KEY = 'AIzaSyDlggHYFZpq69QFa2_F1vE4Clt5bYmAtLA';
		GoogleMapsLoader.load(function(google) {
			var MarkerWithLabel = require('markerwithlabel')(google.maps);
			self.map = new google.maps.Map(document.getElementById('gmap'), {
			  center: {lat:boothmap.lat,lng:boothmap.lng},
			  zoom: boothmap.zoom
			});

			//each booth
			boothmap['maps'].forEach( function(bm){
				var jdata = jsondata[bm.name]
				if( jdata){ //no stage
					var infowindow = new google.maps.InfoWindow({
						content: "<h3><a href='#'>"+jdata.chinese+"</a></h3>" + 
							"<p>"+ jdata.english +"</p>"
					});

					//http://stackoverflow.com/questions/32467212/google-maps-marker-label-with-multiple-characters
					var marker = new MarkerWithLabel({
						position: {lat:bm.lat,lng:bm.lng},
						map: self.map,
						labelContent: bm.num,
						title: bm.name,
						icon: {
							url: "./static/img/clublogo/"+jdata.logo,
							scaledSize: new google.maps.Size(25,25), // scaled size
						},
						labelAnchor: new google.maps.Point(0,0)
					});
				}
				else{
					var infowindow = new google.maps.InfoWindow({
						content: "<h3>"+bm.name+"</h3>" 
					});

					var marker = new MarkerWithLabel({
						position: {lat:bm.lat,lng:bm.lng},
						map: self.map,
						labelContent: bm.name,
						title: "NTUMU",
						icon: {
							url: "./static/img/"+jsondata[ts].logo,
							scaledSize: new google.maps.Size(50,50), // scaled size
						},
						labelAnchor: new google.maps.Point(0,0)
					});
				}

				marker.addListener('click', function() {
					if(self.lastopen)
						self.lastopen.close()
					infowindow.open(this.map, marker);
					self.lastopen = infowindow
				});
			})
		})
	}},
	destroyed: function(){
		GoogleMapsLoader.release();
	},
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
