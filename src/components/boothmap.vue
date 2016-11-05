<template>
	<div id="boothmap">
		<div id="gmap"></div>
	</div>
</template>

<style scoped>
#boothmap{
	height: 80vh;
	width: 95vw;
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
export default {
	name: 'boothmap',
	data(){ return {
		map:null,
		lastopen:null
	}},
	created: function(){
		$(".title-word").html("武聯-攤位地圖")
	},
	mounted: function(){
		var self = this.$data;
		var jsondata = window.clubsdata,
			ts = window.ts,
			clubname = window.clubname

        self.map = new google.maps.Map(document.getElementById('gmap'), {
          center: {lat:jsondata[ts]['boothmap'].lat,lng:jsondata[ts]['boothmap'].lng},
          zoom: jsondata[ts]['boothmap'].zoom
        });
		jsondata[ts]['boothmap']['maps'].forEach( function(bm){
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
						url: "./../static/img/clublogo/"+jdata.logo[0].src,
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
						url: "./../static/img/"+jsondata[ts].logo,
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
	}
}
</script>
