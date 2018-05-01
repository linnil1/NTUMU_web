<template>
  <div class="table-all" id="course">
    <table-event :table="table" :eventdata="eventdata"> </table-event>
  </div>
</template>

<style scoped>
.table-all >table{
  margin: 20px auto;
  max-width: 80vw;
  max-height: calc(100vh - 50px - 40px);
}
@media only screen and (max-width: 768px) {
  .table-all >table{
    margin: 0 auto;
    max-width: 100vw ;
    max-height: calc(100vh - 50px );
  }
}

</style>
<style>
.event:hover{
  opacity: 0.6;
  cursor: cell;
}
.hiddencol{
  max-width: 80vw !important;
}
.hiddenrow > div{
  max-height: calc(100vh - 50px - 40px - 1.3em - 2px) !important;
}
.coldivs{
  height: 1.3em;
}
@media only screen and (max-width: 768px) {
  .hiddencol{
    max-width: calc( 100vw - 3.5em - 2px ) !important;
  }
  .hiddenrow > div{
    max-height: calc(100vh - 50px - 1.3em - 2px) !important;
  }
}
</style>

<script>
import TableEvent from './drag-table/TableEvent';

var weeknames = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
var weekGet = function (weekstr) {
  return weeknames.indexOf(weekstr.trim());
};
var
  timeGet = function (time) {
    var regans = /(\d+):(\d+)/g.exec(time);
    return regans[1] * 60 + 1 * regans[2];
  };
var

  intervalGet = function (twotimes) {
    var arr = twotimes.split('~');
    if (arr.length === 1) { arr.push('22:00'); }
    return [timeGet(arr[0]), timeGet(arr[1])];
  };

export default {
  name: 'course',
  props: ['ver'],
  components: {
    TableEvent
  },
  data: function () {
    return {
      table: {
        width: 40,
        rows: weeknames,
        cols: []
      },
      eventdata: []
    };
  },
  methods: {
    create: function () {
      this.table.cols = [];
      this.eventdata = [];

      for (var i = 6; i <= 22; ++i) {
        this.table.cols.push(i + ':00');
        this.table.cols.push('');
      }
      $('.title-word').html('武聯-課表');
      var self = this.$data;
      var jsondata = this.$store.state.clubsdata;
      var ts = this.ver;
      var events = [];
      // put data into weeks array
      var color = ['#FDF3E7', '#DFE2DB', '#FFF056', '#F3FAB6', '#CBE32D', '#ECECEA', '#92E1C0', '#FAD165', 'rgb(179, 220, 108)', '#42D692', 'rgb(255, 173, 70)', 'rgb(154, 156, 255)', '#B99AFF'];
      // hoverfunc = this.hoverfunc;
      jsondata[ts].clubs.forEach(function (clubname) {
        var club = jsondata[clubname];
        club[ts].course.forEach(function (cour) {
          var timearr = cour['time'].split(',');
          var time = intervalGet(timearr[1]);
          events.push({
            start: time[0] / 30 - 12,
            end: time[1] / 30 - 12,
            row: weekGet(timearr[0]),
            title: club[ts].chinese + '(' + cour.title + ')',
            bgcolor: color[parseInt(club[ts].english[0], 36) % color.length],
            clickfunc: function (domevt) {
              console.log(domevt);
              var dom = $(domevt.target);
              if (!dom.data('bs.popover')) {
                dom.popover({
                  html: true,
                  container: 'body',
                  placement: 'bottom',
                  trigger: 'none', // overwrite
                  // delay: {hide: 500},
                  title: '<h5>' + club[ts].chinese + '</h5>',
                  content: '<span>' + cour.title + '<br>' + cour.place + '<br>' + cour.time + '</span>'
                });
              }
              dom.popover('toggle');
            }
          });
        });
      });
      self.eventdata = events;
      this.$nextTick(function () {
      // center important data
        var helper = $('#drag-table');
        var left = helper[0].clientWidth - helper[0].scrollWidth + 30;
        helper.css('left', left);
        $('#cols-move-id').css('left', left);
      });
      window.scrollTo(0, 0);// scroll to top when load
    }},
  created: function () { // not very well methods for reused component
    $('.popover').hide();
    this.create();
  },
  watch: {
    '$route' (to, from) {
      $('.popover').hide();
      this.create();
    }
  },
  destroyed: function () {
    $('.popover').hide();
  }
};
</script>
