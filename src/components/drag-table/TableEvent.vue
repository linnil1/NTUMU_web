<template>
  <table>
    <tr>
      <!-- top left -->
      <td class="col-allow-hidden"></td>

      <!-- top row = Time -->
      <td class="col-allow-hidden" style="position:relative">
        <div class="col-gradient"><!-- for grandient -->
          <div id="timeline-block-id" class="timeline-block">
            <div v-for="col in table.cols"
               v-bind:key="col"
               class="coldiv"
               :style="{width:table.width+'px'}">
              <span class="timeline-title">{{col}}</span>
            </div>
          </div>
        </div>
      </td>
    </tr>

    <!-- For each row -->
    <tr>
      <!-- First column as Weekday name -->
      <td class="row-allow-hidden" style="position:relative">
        <div class="row-gradient"><!-- for grandient -->
          <div id="weekname-block-id" class="weekname-block">
            <div v-for="(row,i) in table.rows"
               v-bind:key="row"
               class="timeline-title"
               :style="{height: rowheight[i] * 1.5 + 'em'}">
              <span class="weekname-title">{{row}}</span>
            </div>
          </div>
        </div>
      </td>

      <!-- Events in the day -->
      <td class="col-allow-hidden row-allow-hidden drag-table-div" >
        <div>
          <div id="drag-table"
               :style="{width:table.width * (table.cols.length - 1) + 'px'}">
            <one-row-event v-for="(row,i) in table.rows"
                     :style="{height: rowheight[i] * 1.5 + 'em'}"
                     :width="table.width"
                     :cols="table.cols.length - 2"
                     :events ="rowFilter(i)"
                     :key ="rowFilter(i)"
                     v-model:height="rowheight[i]"></one-row-event>
          </div>
        </div>
      </td>
    </tr>
  </table>
</template>


<script>
import OneRowEvent from './OneRowEvent';

export default {
  name: 'TableEvent',
  props: {
    table: {
      type: Object,
      default: () => ({
        width: 60,
        cols: ['col'],
        rows: ['row']
      })
    },
    eventdata: {
      type: Array,
      default: () => []
    }
  },
  data () {
    return {
      rowheight: [],
    };
  },
  created: function () {
    this.rowheight = [];
    for (var i = 0; i < this.table.rows.length; ++i) {
      this.rowheight.push(1);
    }
  },
  components: {
    OneRowEvent
  },
  methods: {
    rowFilter: function (row) {
      return this.eventdata.filter((data) => data.row === row);
    },
  },
  mounted: function () {
    this.$nextTick(function () {
      window.$('#drag-table').draggable({
        cursor: 'grab',
        drag: function (event, ui) {
          // console.log(ui.position)
          // no blank bound
          var helper = ui.helper[0];
          ui.position.top = Math.min(0, ui.position.top);
          ui.position.left = Math.min(0, ui.position.left);
          // console.log(helper);
          ui.position.top = Math.max(
            helper.parentNode.clientHeight - helper.scrollHeight, ui.position.top);
          ui.position.left = Math.max( // rightest border cannot see
            helper.parentNode.clientWidth - helper.scrollWidth, ui.position.left);
          // console.log('calc', ui.position);
          // move col and row
          document.querySelector('#timeline-block-id').style.left = ui.position.left + 'px';
          document.querySelector('#weekname-block-id').style.top  = ui.position.top  + 'px';
        }
      });
    });
  }
};
</script>


<style scoped>
.col-allow-hidden > div {
  overflow-x: hidden;
  max-width: 80vw;
}
.row-allow-hidden > div {
  overflow-y: hidden;
  vertical-align: top;
  max-height: 80vh;
}

@media only screen and (max-width: 768px) {
  .col-allow-hidden > div {
    max-width:  calc( 100vw - 3.5em - 2px );
  }
  .row-allow-hidden > div {
    max-height: calc( 100vh - 50px - 1.4em);
  }
}

.timeline-block{
  height: 1.3em;
  white-space: nowrap;
  position: relative;
}
.weekname-block{
  white-space: nowrap;
  position: relative;
}

.timeline-title{
  text-align: right;
  padding-right: .5em;
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;
  white-space: nowrap;
}
.weekname-title{
}


/*
.col-gradient:after, .row-gradient:after {
  width: 100%;
  height: 100%;
    position: absolute;
    content: "";
    top: 0;
    left: 0;
}
.col-gradient:after{
  background: linear-gradient(90deg,
    rgba(255,255,255,.75) 0%,
    rgba(255,255,255,0) 10%,
    rgba(255,255,255,0) 90%,
    rgba(255,255,255,.75) 100% );
}
.row-gradient:after {
  background: linear-gradient(180deg,
    rgba(255,255,255,.75) 0%,
    rgba(255,255,255,0) 10%,
    rgba(255,255,255,0) 90%,
    rgba(255,255,255,.75) 100% );
}
*/

.drag-table-div{
  border:solid #aaa;
  border-width:2px 0 0 2px;
}
.coldiv{
  display: inline-block;
  vertical-align: top;
  overflow: hidden;
  width: 60px;
  padding-bottom: .5em;
}

#drag-table{
}
</style>
