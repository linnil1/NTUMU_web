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
import {Loader} from 'google-maps';

export default {
  name: 'boothmap',
  props: ['ver'],
  data () {
    return {
      map: null,
      lastopen: null
    };
  },
  methods: {
    create: async function () {
      this.$store.commit('titleSet', '武聯-攤位地圖');
      var self = this.$data;
      var jsondata = this.$store.state.clubsdata;
      var ts = this.ver;
      var boothmap = jsondata[ts]['boothmap'];
      const loader = new Loader('AIzaSyDlggHYFZpq69QFa2_F1vE4Clt5bYmAtLA');
      const google = await loader.load();
      self.map = new google.maps.Map(document.getElementById('gmap'), {
        center: {lat: boothmap.lat, lng: boothmap.lng},
        zoom: boothmap.zoom
      });

      // each booth
      var MarkerWithLabel = require('markerwithlabel')(google.maps);
      boothmap['maps'].forEach(function (bm) {
        var jdata = jsondata[bm.name];
        var infowindow;
        var marker;
        if (jdata) { // no stage
          infowindow = new google.maps.InfoWindow({
            content: "<h3><a href='/" + ts + "/club/" + jdata.name + "'>" + jdata.chinese + '</a></h3>' +
            '<p>' + jdata.english + '</p>'
          });
          console.log(jdata.name);

          // http://stackoverflow.com/questions/32467212/google-maps-marker-label-with-multiple-characters
          marker = new MarkerWithLabel({
            position: {lat: bm.lat, lng: bm.lng},
            map: self.map,
            labelContent: bm.num,
            title: bm.name,
            icon: {
              url: '/static/img/clublogo/' + jdata.logo,
              scaledSize: new google.maps.Size(25, 25) // scaled size
            },
            labelAnchor: new google.maps.Point(0, 0)
          });
        } else {
          infowindow = new google.maps.InfoWindow({
            content: '<h3>' + bm.name + '</h3>'
          });

          marker = new MarkerWithLabel({
            position: {lat: bm.lat, lng: bm.lng},
            map: self.map,
            labelContent: bm.name,
            title: 'NTUMU',
            icon: {
              url: '/static/img/' + jsondata[ts].logo,
              scaledSize: new google.maps.Size(50, 50) // scaled size
            },
            labelAnchor: new google.maps.Point(0, 0)
          });
        }

        marker.addListener('click', function () {
          if (self.lastopen) { self.lastopen.close(); }
          infowindow.open(this.map, marker);
          self.lastopen = infowindow;
        });
      });
    window.scrollTo(0, 0);// scroll to top when load
    }
  },
  unmount: function () {
    // GoogleMapsLoader.release();
  },
  created: function () { // not very well methods for reused component
    // GoogleMapsLoader.release();
    this.create();
  },
  watch: {
    '$route' () {
      this.create();
    }
  }
};
</script>
