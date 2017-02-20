<template>
	<div class="table-all">
		<table>
			<tr>
				<td></td>
				<td class="tdoverflow">
					<div class="rowline">
						<span class="colstitle" 
							  v-for="i in table.cols+1" 
							  :style="{left:(i-1)*table.width+'px'}">{{i-1}}</span>
					</div>
				</td>
			</tr>
			<tr>
				<td class="tdoverflow">
					<div class="rowline">
						<div v-for="i in table.rows" 
							 class="centertext"
							 :style="colheight[i-1]"> 
							<span>{{i}}</span>
						</div>
					</div>
				</td>
				<td>
					<div>
						<one-row-event v-for="i in table.rows" 
									   :width="table.width" 
									   :cols="table.cols" 
									   :eventdata="rowFilter(i-1)" 
									   :height="colheight[i-1]"></one-row-event>
					</div>
				</td>
			</tr>
		</table>
	</div>
</template>

<style scoped>
.table-all{
	position: relative;
	max-width: 60vw;
	overflow: scroll;
	display: table;
}
.rowline{
	position:relative;
	min-height:1.2em;
}
.tdoverflow{
	overflow: hidden;
}
.colstitle{
	position: absolute;
}
.centertext{
    display: flex;
    justify-content:center;
    align-content:center;
    flex-direction:column; 
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
				cols: 24,
				rows: 7,
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
		for(var i=0; i<this.table.rows;++i){
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
}
</script>

