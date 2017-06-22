<template>
  <div class="background-events" 
       :style="[height,{width:cols*width+1+'px'}]">
    <div class="background-all" 
         :style="height">
      <div class="background-box" 
           :style="{width:width+'px'}"
           v-for="i in cols"></div>
    </div>
    <div class="event" 
         v-for="evt in eventSort"
         v-on:mouseover="evt.hoverfunc"
         v-on:click="evt.clickfunc"
         :style="styleGet(evt)">
      {{evt.title}}</div>
  </div>
</template>

<script>
export default {
  name: 'OneRowEvent',
  props: {
    width: {
      type: Number,
      default: 60
    },
    cols: {
      type: Number,
      default: 16
    },
    data: {
      type: Array,
      default: []
    },
    height: {
      type: Object,
      default: () => ({'height': '1.5em'})
    }
  },
  methods: {
    styleGet: function (evt) {
      return {
        left: evt.start * this.width + 'px',
        width: (evt.end - evt.start) * this.width + 'px',
        top: evt.rank + 'em',
        color: evt.color,
        'background-color': evt.bgcolor
      };
    }
  },
  computed: {
    eventSort: function () {
      // data(){return {eventdata=this.dat}} is not data-bind
      var eventdata = JSON.parse(JSON.stringify(this.data));
      for (var i in eventdata) {
        eventdata[i].clickfunc = this.data[i].clickfunc || function () {};
        eventdata[i].hoverfunc = this.data[i].hoverfunc || function () {};
      }
      if (!eventdata.length) { return []; }
      // sorted from first to last
      var sortedevent = eventdata; // deepcopy
      sortedevent.sort(function (a, b) {
        if (a.start !== b.start) { return a.start > b.start; } else { return a.end > b.start; }
      });
      // set sorted rank
      var queue = [];
      for (var e in sortedevent) {
        var evt = sortedevent[e];
        var isput = false;
        for (var q in queue) {
          if (queue[q] <= evt.start) {
            queue[q] = evt.end;
            evt.rank = q * 1.5;
            isput = true;
            break;
          }
        }
        if (!isput) {
          evt.rank = 1.5 * queue.length;
          queue.push(evt.end);
        }
      }
      // hightest rank
      this.height.height = queue.length * 1.5 + 'em';
      return sortedevent;
    }
  }
};
</script>

<style scoped>
.background-box{
  border-right: 1px solid #ddd;
  float: left;
  width: 60px;
  height: 100%;
}
.background-box:nth-child(odd){
  border-right: 1px dotted #ddd;
}
.background-all{
  border: 1px solid #ddd;
  border-right: 0;
  position: relative;
  z-index: -5;
  overflow: hidden;
  height: 3em;
}
.background-events{
  position: relative;
  width: 100%;
}
.event{
  position: absolute;
  background-color: #9f3;
  height: 1.5em;
  text-align: center;
  font-size: 1em;
  overflow: hidden;
}
</style>
