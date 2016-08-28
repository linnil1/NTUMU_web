
var home_html = `
	<div id="slideshow" class="carousel slide" data-ride="carousel">
		<style>
#slideshow{
	width:70%;	
	height:500px;
	margin:auto;
}
		</style>
		<div class="carousel-inner" role="listbox" 
			style="display:block">
			<div v-bind:class="['item',$index==0 ? 'active' : '']" 
				 v-for="count in counts">
				<img class="img-responsive" v-bind:src="count.imgsrc" alt="" 
					 style="max-height:500px;margin:auto">
				<div class="carousel-caption">
					<h3>{{count.title}}</h3>
					<p> {{count.desp}} </p>
				</div>
			</div>
		</div>
		<a class="left carousel-control" href="#slideshow" role="button" data-slide="prev">
			<span class="glyphicon glyphicon-chevron-left" aria-hidden=""></span>
		</a>
		<a class="right carousel-control" href="#slideshow" role="button" data-slide="next">
			<span class="glyphicon glyphicon-chevron-right" aria-hidden=""></span>
		</a>
	 </div>
 `

 var home_vue = {
	el : "#slideshow",
	data : {
		counts : [ {
			imgsrc : "img/countdown/count1.jpg",
			title  : "countdown #1 day",
			desp   : "NTU YangTa is good"
		}, {
			imgsrc : "img/countdown/count2.jpg",
			title  : "countdown #2 day",
			desp   : "NTU YangTa is good"
		}, {
			imgsrc : "img/countdown/count3.jpg",
			title  : "countdown #3 day",
			desp   : "NTU YangTa is good"}]
	}
}

var course_html = `
<style>
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
	margin: auto;
	font-size: 20px;
	overflow: scroll;
	position: relative;
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
	border: 1px solid green ;
	margin: 0px;
	background-color: #9f3;
	width : 48px;
	font-size: 15px;
    word-wrap: break-word;
	overflow: hidden;
}

</style>

<div class="row">
	<div class="col-sm-3"></div>
	<div class="col-sm-6" id="main">
		<table id="course">
			<tr>
				<th></th>
				<th v-for="wn in weekname" style="text-align:center">{{wn.slice(2,3)}}</th>
			</tr>
			<tr style="height:1px;">
				<td style="width:60px;"></td>
				<td colspan="7">
					<div class="background-all">
						<div class="background-hour">
							<div class="background-box" v-for="i in 14">
								<div class="background-devide"></div>
							</div>
						</div>
					</div>
				</td>
			</tr>
			<tr>
				<td>
					<div class="coursetime" v-for="i in 14">{{i+8+":00"}}</td>
				</td>
				<td class="day" v-for="wevt in weekevents"> 
					<div style="position:relative" v-bind:style="daywidth[$index]">
						<div class="event" v-for="evt in wevt" v-on:mouseover="hoveOnevent(evt,$event)" v-bind:style="evt.style">
							<span>{{evt.name}}</span>
							<span style="font-size:small">{{"("+evt.title+")"}}</span>
						</div>
					</div>
				</td>
			</tr>
		</table>
	</div>
	<div class="col-sm-3"></div>
</div>
`

var course_vue = {
	el : "#course",
	data : {
		weekname: weeknames,
		timepx  : 42,
		widthpx : 48
	},
	created: function(){
		var events = [ [],[],[],[],[],[],[] ]
		var data = {
			楊氏廣法太極拳社:{
				courses : [ { 
					time :'星期六, 18:00~21:00',
					title:'社課'},{
					time:'星期三, 18:30~21:30',
					title: '團練'},{
					time:'星期六, 15:30~17:30',
					title: 'test'}]
			},
			少林拳社:{
				courses : [ { 
					time :'星期六, 17:00~22:00',
					title:'社課'}]
			},
			國術社:{
				courses : [ { 
					time :'星期六, 19:20~20:10',
					title:'社課'}]
			}}

		// put data into weeks array
		for(var dname in data) {
			var courses = data[dname].courses
			for(var course in courses) {
				var cour = courses[course]
				var timearr = cour['time'].split(',')
				events[ weekGet( timearr[0] ) ].push({
						style : intervalGet(timearr[1],this.timepx),
						name  : dname,
						title : cour.title,
						time  : cour.time,

				})
			}
		}

		// sorted
		for(var evt in events)
			events[evt].sort(function(a,b){return a.style.top > b.style.top})

		//find min lines
		this.daywidth = []
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
				tmp.style.left = this.widthpx*line + "px"
				endtimes[line] = pxRemove(tmp.style.top) + pxRemove(tmp.style.height)
			}
			// find each day width
			dayw = endtimes.length*this.widthpx
			if( dayw == 0)
				dayw = this.widthpx
			this.daywidth[evt]={width:dayw+"px"}
		}
		this.weekevents = events
	},
	destroy: function(){
		alert("123")
	},
	methods:{
		hoveOnevent: function(evt,domevt){
			dom = $(domevt.target)
			if( dom.prop("tagName").toLowerCase() != "div")
				return
			console.log(dom)
			dom.popover({
				html : true, 
				container: 'table',
				trigger:"hover",

				title: "<a href=''>"+evt.name+"</a>",
				content:"<p>"+evt.title+"<br>"+evt.time+"</p>",
			})
			dom.popover('show')
		}
	}
}

var weeknames = ['星期日','星期一', '星期二', '星期三', '星期四', '星期五', '星期六']


weekGet = function(weekstr){
	return weeknames.indexOf(weekstr.trim())
}

intervalGet = function(twotimes,timepx){
	var arr =  twotimes.split('~')
	var start = pxGet(arr[0],timepx)
	var end   = pxGet(arr[1],timepx)
	return {
		top: start+"px",
		height: end-start+"px"
	}
}


pxGet = function(yourtime,timepx){
	var arr = yourtime.split(':')
	var hour = arr[0]|0
	var mins = arr[1]|0
	return (hour*60+mins-480)*timepx/60
}

pxRemove = function(text){
	return text.slice(0,-2)|0
}


