<template>
  <div class="table-all">
    <table-event :table="table" :eventdata="eventdata"> </table-event>
  </div>
</template>

<style scoped>
.table-all{
  margin: auto;
  max-width: 600px;
  max-height: 400px;
}
</style>
<style>
.hiddencol{
  max-width: 600px !important;
}
.hiddenrow > div{
  max-height: 400px !important;
}
</style>
<script>

import TableEvent from './TableEvent';
var clubsdata = require('./clubs.json');
var weeknames = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];

var
  weekGet = function (weekstr) {
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
  name: 'TimeLineTest',
  data () {
    return {
      table: {
        width: 40,
        rows: weeknames,
        cols: []
      },
      eventdata: []
    };
  },
  created: function () {
    for (var i = 6; i <= 22; ++i) {
      this.table.cols.push(i + ':00');
      this.table.cols.push(i + ':30');
    }
    var events = [];
    var
      self = this.$data;
    var
      jsondata = clubsdata;
    var
      ts = '105_1';

    // put data into weeks array
    var
      color = ['#FDF3E7', '#DFE2DB', '#FFF056', '#F3FAB6', '#CBE32D', '#ECECEA', '#92E1C0', '#FAD165', 'rgb(179, 220, 108)', '#42D692', 'rgb(255, 173, 70)', 'rgb(154, 156, 255)', '#B99AFF'];
    // var hoverfunc = this.hoverfunc;
    jsondata[ts].clubs.forEach(function (clubname) {
      var club = jsondata[clubname];
      console.log(club);
      club[ts].course.forEach(function (cour) {
        var timearr = cour['time'].split(',');
        var time = intervalGet(timearr[1]);
        events.push({
          start: time[0] / 30 - 12,
          end: time[1] / 30 - 12,
          row: weekGet(timearr[0]),
          title: club.chinese + '(' + cour.title + ')',
          bgcolor: color[parseInt(club.english[0], 36) % color.length],
          clickfunc: function (domevt) {
            var dom = $(domevt.target);
            if (!dom.data('bs.popover')) {
              dom.popover({
                html: true,
                container: 'body',
                placement: 'bottom',
//                trigger: "click",
                // delay: {hide: 500},

                title: '<h5>' + club.chinese + '</h5>',
                content: '<span>' + cour.title + '<br>' + cour.place + '<br>' + cour.time + '</span>'
              });
            }
            dom.popover('toggle');
          }
        });
      });
      self.eventdata = events;
    });
    window.scrollTo(0, 0);// scroll to top when load
  },
  components: {
    TableEvent
  },
  mounted: function () {
    // center important data
    var helper = $('#drag-table');
    var left = helper[0].clientWidth - helper[0].scrollWidth;
    helper.css('left', left);
    $('#cols-move-id').css('left', left);
  },
  methods: {
  },
  computed: {
  }
};
</script>

