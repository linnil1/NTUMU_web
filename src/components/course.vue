<template>
	<div class="container-fluid" id="course" >
		<!-- button -->
		<div>
			<!-- clear -->
			<div class="btn-group">
				<button type="button" class="btn btn-warning" v-on:click="showClear('')">clear</button>
				<button type="button" class="btn btn-warning dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
					<span class="caret"></span>
				</button>
				<ul class="dropdown-menu">
					<li><a v-on:click.prevent="showClear('club')" href="#">clear club</a></li>
					<li><a v-on:click.prevent="showClear('day')" href="#">clear day</a></li>
				</ul>
			</div>
	
			<!-- show -->
			<div class="btn-group">
				<button type="button" class="btn btn-success" v-on:click="showAll('')">all</button>
				<button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
					<span class="caret"></span>
				</button>
				<ul class="dropdown-menu">
					<li><a v-on:click.prevent="showAll('club')" href="#">show club</a></li>
					<li><a v-on:click.prevent="showAll('day')" href="#">show day</a></li>
				</ul>
			</div>
	
			<!-- clubs -->
			<div class="btn-group">
			    <button type="button" class="btn btn-info dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				club <span class="caret"></span>
			    </button>
				<div class="dropdown-menu" style="min-width : 180px" >
					<div v-for="club in clublist">
						<input type="checkbox" v-bind:id="'club_'+club.name" v-bind:value="club.name" v-model="showclub">
						<label v-bind:for="'club_'+club.name">{{club.chinese}}</label>
					</div>
			    </div>
			</div>
	
			<!-- days -->
			<div >
				<span v-for="(name,index) in weekname">
					<input type="checkbox" v-bind:id="'day_'+index" v-bind:value="index" v-model="showday">
					<label v-bind:for="'day_'+index">{{name.slice(2,3)}}</label>
				</span>
			</div>
	
			<!-- <button type="button" class="btn btn-default" v-on:click.prevent="urlGo('app=coursedrag')">
				<span class="glyphicon glyphicon-retweet"></span> 
				computer version</button> -->
		</div>
	
		<!-- table -->
		<div class="course-div">
			<table>
				<tr>
					<th></th>
					<th v-for="sd in sortedshowday" style="text-align:center">{{weekname[sd].slice(2,3)}}</th>
				</tr>
				<tr style="height:1px;">
					<td style="width:60px;"></td>
					<td colspan="7">
						<div class="background-all">
							<div class="background-hour">
								<div class="background-box" v-for="i in 16">
									<div class="background-devide"></div>
								</div>
							</div>
						</div>
					</td>
				</tr>
				<tr>
					<td>
						<div class="coursetime" v-for="i in 16">{{i+5+":00"}}</td>
					</td>
					<td class="day" v-for="sd in sortedshowday"> 
						<div style="position:relative" v-bind:style="daywidth[sd].style">
							<div class="event" v-for="evt in showevents[sd]" v-on:mouseover="hoverOnevent(evt,$event)" v-bind:style="evt.style">
								<span>{{evt.chinese}}</span>
								<span style="font-size:small">{{"("+evt.course.title+")"}}</span>
							</div>
						</div>
					</td>
				</tr>
			</table>
		</div>
	</div>
</template>

<style scoped>
.background-devide{
	border-bottom: 1px dotted #ddd;
	border-top: 1px solid #ddd;
	height:21px;
}
.background-box{
	height:42px;
}
.background-all{
	position: relative;
	z-index : -5;
}
.background-hour{
	position: absolute;
	width: 100%;
}

table{
/*	empty-cells:show;
	border: 1px solid black; */
	font-size: 20px;
	overflow: scroll;
	position: relative;
	margin: 10px;
}
tr td{
	min-width : 48px;
	/*
	width: 42px;
  border: 1px solid black; 

	display: table-cell; */
}

.coursetime{
	height:42px;
	text-align: right;
	vertical-align: top;
	padding: 1px 2px 0 0;
	border: 0;
	position: relative;
	top: -10px;
}
.day{
	border-right : 1px solid #ddd;
	vertical-align: top;
}
.event{
	vertical-align: top;
	display: inline-block;
	position: absolute;
	border: 0;
	margin: 0px;
	background-color: #9f3;
	width : 48px;
	font-size: 15px;
	word-wrap: break-word;
	overflow: hidden;
}

.course-div{
	margin: 10px;
//	height: 80vh;
	overflow: scroll;
}
.course-div::-webkit-scrollbar { // this not show on firefox QQ
	width: 1em;
	height: 1em;
}
 
.course-div::-webkit-scrollbar-track {
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
}
.course-div::-webkit-scrollbar-thumb {
  background-color: darkgrey;
  outline: 1px solid slategrey;
}

</style>

<script>
var weeknames = ['星期日','星期一', '星期二', '星期三', '星期四', '星期五', '星期六']

var weekGet = function(weekstr){
	return weeknames.indexOf(weekstr.trim())
}
var intervalGet = function(twotimes,timepx){
	var arr =  twotimes.split('~')
	var start = pxGet(arr[0],timepx)
	if(arr.length==1)
		arr.push("22:00")
	var end   = pxGet(arr[1],timepx)
	return {
		top: start+"px",
		height: end-start+"px"
	}
}

var pxGet = function(yourtime,timepx){
	var arr = yourtime.split(':')
	var hour = arr[0]|0
	var mins = arr[1]|0
	return (hour*60+mins-360)*timepx/60
}

var pxRemove = function(text){
	return text.slice(0,-2)|0
}

export default {
	name: 'course',
	data(){ return {
		weekname: weeknames,
		showday : [0,1,2,3,4,5,6],  //sorted
		showclub : [],
		clublist : [],
		timepx  : 42,
		widthpx : 48,
		daywidth : [{style:{}},{style:{}},{style:{}},{style:{}},{style:{}},{style:{}},{style:{}}],  // bug
		allevents: [],
		wantevents : []
	}},
	created: function(){
		$(".title-word").html("武聯-課表")

		var events = [ [],[],[],[],[],[],[] ]
		
		var self = this.$data
		var jsondata = window.clubsdata,
			ts = window.ts,
			clubname = window.clubname

		// put data into weeks array
		var clubs =[]
		self.clublist = [] // bug
		jsondata[ts].clubs.forEach(function(clubname){
			var club = jsondata[clubname]
			self.clublist.push( {
				name:    clubname,
				chinese: club.chinese
			})
			clubs.push(clubname)
						

			club.course[0].courses.forEach(function(cour){
				var timearr = cour['time'].split(',')
				events[ weekGet( timearr[0] ) ].push({
						style  : intervalGet(timearr[1],self.timepx),
						chinese: club.chinese,
						name   : clubname,
						course : cour
				})
			})
			self.allevents = events
			self.showclub = clubs
		})
	},
	computed: {
		sortedshowday: function(){
			return this.$data.showday.sort(function(a,b){return a-b})
		},
		showevents: function(){
			// bind with club
			var clubs = this.$data.showclub ,
				wants = [[],[],[],[],[],[],[]]
			for(var d in this.allevents){
				this.allevents[d].forEach( function(evt){
					if( clubs.indexOf(evt.name) != -1)
						wants[d].push(evt)
				})
			}

			// reconstruct event
			var events = wants
			// sorted
			for(var evt in events)
				events[evt].sort(function(a,b){return a.style.top > b.style.top})

			var linecolor = ["#92E1C0","#FAD165","rgb(179, 220, 108)","#42D692","rgb(255, 173, 70)","rgb(154, 156, 255)","#B99AFF"]
			//find min lines
			for(var evt in events){
				var endtimes = []
				for(var e in events[evt]){
					var tmp = events[evt][e]
					var line = function(style){
						var i
						for(i in endtimes)
							if( endtimes[i] <= pxRemove(style.top) )
								return i
						return endtimes.length
					}(tmp.style)
					var s = {
						"top"  : tmp.style.top,
						"height"  : tmp.style.height,
						"left" : this.widthpx*line + "px",
						"background-color" : linecolor[line]}
					tmp.style = s  // it can't just set the argument
					endtimes[line] = pxRemove(tmp.style.top) + pxRemove(tmp.style.height)
				}

				// find each day width
				var dayw = endtimes.length*this.widthpx
				if( dayw == 0)
					dayw = this.widthpx
				this.$data.daywidth[evt].style =  {'width': dayw+"px"}
			}
			return events
		}
	},
	methods:{
		hoverOnevent: function(evt,domevt){
			var dom = $(domevt.target)
			if( dom.prop("tagName").toLowerCase() != "div")
				return
//			console.log(dom)
			dom.popover({
				html : true, 
				container: 'body',
				trigger:"hover",
				placement:"top",

				title: "<a href=''>"+evt.chinese+"</a>",
				content:"<span>"+evt.course.title+"<br>"+evt.course.place+"<br>"+evt.course.time+"</span>",
			})
			dom.popover('show')
		},

		showAll: function(wantstr){
			if(wantstr != "club")
				this.$data.showday = [0,1,2,3,4,5,6]
			if(wantstr != "day")
			{
				var clubs = []
				this.clublist.forEach( function( club){
					clubs.push(club.name)
				})
				this.$data.showclub = clubs
			}
		},
		showClear: function(wantstr){
			if(wantstr != "club")
				this.$data.showday = []
			if(wantstr != "day")
				this.$data.showclub = []
		}
	}
}
</script>
