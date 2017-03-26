<template>
	<table>
		<tr>
			<td class="hiddencol"></td>
			<td class="hiddencol" style="position:relative">
				<div class="colsgrad"><!-- for grandient -->
					<div id="cols-move-id" class="coldivs">
						<div v-for="(col,i) in table.cols" 
							 class="coldiv"
							 :style="{width:table.width+'px'}">
							<span class="coltitle">{{col}}</span>
						</div>
					</div>
				</div>
			</td>
		</tr>
		<tr>
			<td class="hiddenrow" style="position:relative">
				<div class="rowsgrad"><!-- for grandient -->
					<div id="rows-move-id" class="rowdivs">
						<div v-for="(row,i) in table.rows" 
							 class="rowdiv"
							 :style="colheight[i]"> 
							<span class="rowtitle">{{row}}</span>
						</div>
					</div>
				</div>
			</td>
			<td class="hiddencol hiddenrow drag-table-div" >
				<div id="drag-table">
					<one-row-event v-for="(row,i) in table.rows" 
								   :width="table.width" 
								   :cols="table.cols.length-1" 
								   :data="rowFilter(i)" 
					               :key ="rowFilter(i)"
								   :height="colheight[i]"></one-row-event>
				</div>
			</td>
		</tr>
	</table>
</template>

<style scoped>
.hiddencol{
	overflow: hidden;
	max-width: 200px;/* should be overwrite by important */
}
.hiddenrow{
	overflow: hidden;
	vertical-align: top;
}
.hiddenrow > div{ /* I don't know why */
	max-height: 200px; /* should be overwrite by important */
}
.drag-table-div{
	border:solid #aaa;
	border-width:2px 0 0 2px;
}
.coltitle{
}
.rowtitle{
}
.coldivs{
	white-space: nowrap;
}
.coldiv{
	display: inline-block;
	vertical-align: top;
	overflow: hidden;
	width: 60px;
	padding-bottom: .5em;
}
.colsgrad:after, .rowsgrad:after {
	width: 100%;
	height: 100%;
    position: absolute;
    content: "";
    top: 0;
    left: 0;
}
.colsgrad:after{
	background: linear-gradient(90deg,
		rgba(255,255,255,.75) 0%,
		rgba(255,255,255,0) 10%,
		rgba(255,255,255,0) 90%,
		rgba(255,255,255,.75) 100% );
}
.rowsgrad:after {
	background: linear-gradient(180deg,
		rgba(255,255,255,.75) 0%,
		rgba(255,255,255,0) 10%,
		rgba(255,255,255,0) 90%,
		rgba(255,255,255,.75) 100% );
}
.rowdivs{
}
.rowdiv{
	text-align: right;
	padding-right: .5em;
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column; 
	white-space: nowrap;
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
				cursor: "grab",
				drag: function( event, ui ) {
					// console.log(ui.position)
					// no blank bound
					var helper = ui.helper[0]
					ui.position.top  = Math.min(0, ui.position.top )
					ui.position.left = Math.min(0, ui.position.left)
					ui.position.top  = Math.max(
						helper.clientHeight - helper.scrollHeight, ui.position.top  )
					ui.position.left = Math.max( // rightest border cannot see
						helper.clientWidth  - helper.scrollWidth, ui.position.left )
					// move col and row
					$("#cols-move-id").css("left",ui.position.left+"px")
					$("#rows-move-id").css("top" ,ui.position.top +"px")
				}
			});
		})
	},
}
</script>

