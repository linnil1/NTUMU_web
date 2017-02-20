<template>
	<table>
		<tr>
			<td class="hiddencol"></td>
			<td class="hiddencol">
				<div id="cols-move-id" class="coldivs">
					<div v-for="(col,i) in table.cols" 
						 class="coldiv"
						 :style="{width:table.width+'px'}">
						<span class="coltitle">{{col}}</span>
					</div>
				</div>
			</td>
		</tr>
		<tr>
			<td class="hiddenrow">
				<div id="rows-move-id" class="rowdivs">
					<div v-for="(row,i) in table.rows" 
						 class="rowdiv"
						 :style="colheight[i]"> 
						<span class="rowtitle">{{row}}</span>
					</div>
				</div>
			</td>
			<td class="hiddencol hiddenrow">
				<div id="drag-table">
					<one-row-event v-for="(row,i) in table.rows" 
								   :width="table.width" 
								   :cols="table.cols.length-1" 
								   :eventdata="rowFilter(i)" 
								   :height="colheight[i]"></one-row-event>
				</div>
			</td>
		</tr>
	</table>
</template>

<style scoped>
.hiddencol{
	overflow: hidden;
	max-width: 60vw;
}
.hiddenrow{
	overflow: hidden;
	vertical-align: top;
}
.hiddenrow > div{ /* I don't know why */
	max-height: 20vh;
}
.coltitle{
}
.rowtitle{
}
.coldivs{
	white-space: nowrap;
}
.rowdivs{
}
.coldiv{
	display: inline-block;
	overflow: hidden;
	min-height: 1.2em;
	width: 60px;
	padding-bottom: .1em;
}
.rowdiv{
	text-align: right;
	padding-right: .5em;
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column; 
}
#cols-move-id, #rows-move-id{
	position: relative;
}
#drag-table{
}
</style>

<script>

import OneRowEvent from './OneRowEvent'

export default {
	name: 'TableEvent',
	props: {
		table: {
			type: Object,
			default: ()=>({
				width: 60,
				cols: ['col'],
				rows: ['row'],
			})
		},
		eventdata: {
			type: Array,
			default: []
		}
	},
	data () { return {
		colheight: [],
		rowdata  : [],
	}},
	created: function(){
		this.colheight = []
		this.rowdata   = []
		for(var i=0; i<this.table.rows.length;++i){
			this.colheight.push({'height':'1.5em'})
			this.rowdata.push([])
		}
	},
	components: {
		OneRowEvent,
	},
	methods: {
		rowFilter: function(row){
			return this.eventdata.filter( (data)=>data.row==row )
		}
	},
	mounted: function(){
		this.$nextTick(function () {
			$( "#drag-table" ).draggable({
				containment: "document",
				cursor: "move",
				drag: function( event, ui ) {
					// console.log(ui.position)
					// no blank bound
					var helper = ui.helper[0]
					ui.position.top  = Math.min(0, ui.position.top )
					ui.position.left = Math.min(0, ui.position.left)
					ui.position.top  = Math.max(
						helper.clientHeight - helper.scrollHeight, ui.position.top  )
					ui.position.left = Math.max( // rightest border cannot see
						helper.clientWidth - $("#cols-move-id")[0].scrollWidth, 
						ui.position.left )
					// move col and row
					$("#cols-move-id").css("left",ui.position.left+"px")
					$("#rows-move-id").css("top" ,ui.position.top +"px")
				}
			});
		})
	},
}
</script>

