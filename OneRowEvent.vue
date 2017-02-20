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
		eventdata: {
			type: Array,
			default: []
		},
		height: {
			type: Object,
			default: ()=>({'height':'1.5em'})
		},
	},
	data () { return {
	}},
	methods: {
		styleGet: function(evt){
			return {
				left: evt.start * this.width + 'px',
				width: (evt.end - evt.start) * this.width + 'px',
				top: evt.rank + 'em',
				color: evt.color,
				'background-color': evt.bgcolor 
			}
		},
	},
	computed: {
		eventSort: function(){
			if(!this.eventdata.length)
				return []
			// sorted from first to last
			var sortedevent = JSON.parse(JSON.stringify(this.eventdata)) //deepcopy
			sortedevent.sort(function(a,b){
				if(a.start != b.start)
					return a.start > b.start
				else
					return a.end > b.start
			})
			// set sorted rank
			var step = 0;
			sortedevent[0].rank = step
			for(var evt in sortedevent)
				if(evt != 0 && sortedevent[evt-1].end > sortedevent[evt].start)
					sortedevent[evt].rank = step += 1.5
				else
					sortedevent[evt].rank = step 
			// hightest rank
			this.height.height = step+1.5+'em'
			return sortedevent
		}
	}
}
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
