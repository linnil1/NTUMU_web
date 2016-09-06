"""
Wanted clubs data (json)

{
    latest: "105-1",
    "105-1":{ #version
        clubs : [""], #clubs name
        countdown: [{src,title,desp}] , #countdown 
        showtime:[ {time,clubname,title} ] , 
        boothmap : {}  # have not think yet
        logo: "", 
    },

    "YangTai": { #clubs name
        name : "YangTai", #same as key
        chinese: "",
        english: "",
        logo: [ {src,ts} ] ,  #sorted latest is first
        course:[
            {ts,courses[{ title,time,place}]}  #course data
            ],  #sorted latest is first
        welcome: [{}], #same as course

        info: [{
            president: "范思晴",
            email : "taida.taichi@gmail.com",
            blog : "taida-taichi.blogspot.com",
            fb : {
                    name : "台大太極拳社 NTU Taichi Club",
                    link : "https://www.facebook.com/台大劍道社-粉絲團-295543953792001/"
            },
            ts : "105-1" #sorted latest is first
        }],

        intro: [{ts,intro=[ {
            id : "short_intro",
            name: "簡介",
            content: ["first","second"], #each pargraph a line 
            },{
            id : "course_intro",
            name: "教學內容",
            content: [ #each pargraph a line 
                    "鄭子太極37式拳架",
                    "熊經、鳥伸等基本養生功"]
            },{
                id: "qa",
                name: "Q-A",
                content:[{
                    q: "question？",
                    a: "answer。"
			}
                    ]
            },{id,name,content} # otherwise content should be html
            ]}],  #sorted latest is first

        longintro: [ {ts,intro=""} ] #i have not do this yet intro may be html
    }
    
}
"""


import json
import csv
import sys
import os.path
from pprint import pprint
import markdown2 as md

def tsFind(data,key,ts):
    if not data.get(key):
        data[key] = []
    allts = data[key]
    for i in allts:
        if(i['ts'] == ts ):
            return i
    allts.insert(0,{'ts':ts})
    return allts[0]

def build(ts):
    want = {
        'latest' : ts,
        ts:{'clubs':[]}
    }
    open("allclubs.json","w").write(json.dumps(want))

def clubUpdate(ts,filename):
    """ csv data
chinese english xxxx name
president email blog fb logo xx
time\nplace\ntitle\n, .... #for course
time\nplace\ntitle\n, .... #for welcome
short_intro course_intro q\na\n ... (title content)
a line for separte each club
    """
    want = json.loads(open("allclubs.json").read())
    if ts > want['latest'] :
        want['latest'] = ts
        want[ts] = {}
    want[ts]['clubs'] = []

    with open(filename,newline='') as f:
        cf = csv.reader(f)
        for i in range(6):  # for header
            cf.__next__()
        while True:
            row = cf.__next__()

            #name
            name = row[3]
            print(name)
            if not want.get(name):
                want[name] = {}
            clubdict = want[name]
            want[ts]['clubs'].append(name)

            #chinese english xxxx name
            clubdict.update({ 
                'name' : name, 
                'chinese' : row[0],
                'english' : row[1]
            })

            #president email blog fb logo xx
            row = cf.__next__()
            info = tsFind(clubdict,'info',ts)
            info.update({
                    'president' : row[0],
                    'email' : row[1],
                    'blog' : row[2],
                    'fb': {},
            })
            if row[3]:
                line = row[3].split('\n')
                info['fb']['name'] = line[0]
                if len(line) > 1:
                    info['fb']['link'] = line[1]
            
            if row[4]:
                logo= tsFind(clubdict,'logo',ts)
                # last modified time append 
                logo['src'] = row[4]+'?'+str(os.path.getmtime("../img/clublogo/"+row[4]))

            #time\nplace\ntitle\n, .... #for course
            def courseRead(name):
                row = cf.__next__()
                course = tsFind(clubdict,name,ts)
                course['courses'] = []
                for c in row:
                    nowc = {}
                    c = [cl for cl in c.split('\n') if cl.strip()]
                    if len(c) < 2:
                        if c:
                            print(c)
                            print("course err")
                        continue
                    if len(c) >= 3:
                        nowc['title'] = c[2]
                    nowc['time'] = c[0]
                    nowc['place'] = c[1]
                    course['courses'].append(nowc)

            courseRead("course")
            courseRead("welcome")
            
            # short_intro course_intro q\na\n... 
            row = cf.__next__()
            intro = tsFind(clubdict,'intro',ts)
            intro['intro'] = [{
                'id' : "short_intro",
                'name' : "簡介",
                'content' : list(filter(None,row[0].split('\n')))
            },{
                'id' : "course_intro",
                'name' : "教學內容",
                'content' : list(filter(None,row[1].split('\n')))
            }]
            
            qas = list(filter(None,row[2].split('\n')))
            qalist = []
            for line in range(0,len(qas),2):
                qalist.append({
                    'q':qas[line][1:],  #remove Q A
                    'a':qas[line+1][1:]
                })

            intro['intro'].append({
                'id' : "qa",
                'name' : "Q-A",
                'content' : qalist
            })

            # other desp should be markdown format
            for i in range(3,len(row)):
                if row[i].strip() == "" :
                    continue;
                rowtitle = row[i].split("\n")[0]
                intro['intro'].append({
                    'id' : rowtitle,
                    'name' : rowtitle,
                    'content' : md.markdown(row[i][row[i].find('\n')+1:])
                })


            #remove blank content 
            intro['intro'][:] = [ it for it  in intro['intro'] if it['content']]

            #a line for separte each club
            try:
                row = cf.__next__()
            except:
                break;

            #pprint(clubdict)

    want[ts]['clubs'].sort()
    open("allclubs.json","w").write(json.dumps(want))


def commonUpdate(ts,filename):
    """ 
csv data
countdown
name title src desp
...

booth
name lonlat number
...

name
time name title
...

    """
    want = json.loads(open("allclubs.json").read())
    with open(filename,newline='') as f:
        cf = list(csv.reader(f))

        #classify data
        data = {}
        index = 0
        while index < len(cf):
            start = index
            while index < len(cf) and cf[index][0]:
                index += 1
            data[ cf[start][0] ] = cf[start:index]
            while index < len(cf) and cf[index][0] == '':
                index += 1

        #showtime
        want[ts]['showtime'] = {
                'title' : data['showtime'][0][1],
                'where' : data['showtime'][0][2],
                'shows' : []
        }
        for show in data['showtime'][1:]:
            want[ts]['showtime']['shows'].append({
                'time': show[0],
                'name': show[1],
                'title': show[2]
            })

        #map
        want[ts]['boothmap'] = {
                'lat':float(data['booth'][0][1]),
                'lng':float(data['booth'][0][2]),
                'zoom':float(data['booth'][0][3]),
                'maps':[]
                }
        for booth in data['booth'][1:]:
            want[ts]['boothmap']['maps'].append({
                'name': booth[0],
                'lng': float(booth[1].split(',')[1]),
                'lat': float(booth[1].split(',')[0]),
                'num': booth[2]
            })
        
        #countdown
        want[ts]['countdown'] = []
        for count in data['countdown'][1:]:
            want[ts]['countdown'].append({
                'name': count[0],
                'title': count[1],
                'src' : count[2] +'?'+str(os.path.getmtime("../img/countdown/"+count[2])),
                'fullsrc' : count[3],
                'desp': "<br>".join(count[4].split("\n"))
            })
    
    want[ts]['logo'] = ts+"_logo.png"
    for i in want[ts]:
        print(i)
    open("allclubs.json","w").write(json.dumps(want))


myarg = sys.argv[1:]
print(myarg)
if len(myarg) == 0 :
    raise TypeError("no operation")
if len(myarg) == 1 :
    raise TypeError("no ts")
if myarg[0] == "build":
    build(myarg[1])
    exit()
if len(myarg) == 2 :
    raise TypeError("no path")

if myarg[0] == "clubUpdate":
    clubUpdate(myarg[1],myarg[2])
elif myarg[0] == "commonUpdate":
    commonUpdate(myarg[1],myarg[2])
else:
    raise TypeError("error operation")
    
""" example
build("105_1")
clubUpdate("105_1","105_1_club.csv")
commonUpdate("105_1","105_1_common.csv")
"""

