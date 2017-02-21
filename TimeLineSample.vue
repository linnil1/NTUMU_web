<template>
	<div class="table-all">
		<table-event :table="table" :eventdata="eventdata"> </table-event>
	</div>
</template>

<style scoped>
.table-all{
	margin: auto;
	max-width: 300px;
	max-height: 100px;
}
</style>
<style>
.hiddencol{
	max-width: 300px !important;
}
.hiddenrow > div{
	max-height: 100px !important;
}
</style>
<script>

import TableEvent from './TableEvent'

export default {
	name: 'TimeLineSample',
	data () { return {
		table:{
			width: 60,
			cols: ["123124323523","345","123","123","123","123","345","345","kk"], //odd
			rows: ["123456789","345","567","789","345","567","789"],
		},
		eventdata: [{
			start: 4.,
			end: 5.3,
			row: 0,
			bgcolor: 'red',
			title: "Hello",
			clickfunc: function(domevt){
				alert("click")
			}
		},{
			start: 4,
			end: 5.3,
			row: 0,
			title: "Hover ON Me",
			hoverfunc: function(domevt){
				$(domevt.target).text("Hover")
				setTimeout( ()=>
					( $(domevt.target).text("Not Hover") ),1000
				)
			}
		},{
			start: 0,
			end: 2.4,
			row: 2,
			title: "Hello"
		},{
			start: 6,
			end: 6.2,
			row: 3,
			title: "Hello"
		}],
	}},
	created: function(){
	},
	components: {
		TableEvent,
	},
	mounted: function(){
	},
	methods: {
	},
	computed: {
	}
}
</script>

