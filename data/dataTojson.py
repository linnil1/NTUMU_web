"""
Wanted clubs data (json)

{
    latest: "105-1",
    "105-1":{ #version
        clubs : [""], #clubs name
        slideshow: [{src,title,desp}] , #countdown 
        location : {}  # have not think yet
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

""" csv data
chinese english xxxx key
president email blog fb logo xx
time\nplace\ntitle\n, .... #for course
time\nplace\ntitle\n, .... #for welcome
short_intro course_intro q\na\n... 
a line for separte each club
"""

import json
import csv
from pprint import pprint

latest = "105_1"

want = {
        'latest' : latest,
        latest:{'clubs':[]}
}

def tsFind(allts,ts=latest):
    for i in allts:
        if(i['ts'] == ts ):
            return i
    allts.insert(0,{'ts':ts})
    return allts[0]

with open("105_1_club.csv",newline='') as f:
    cf = csv.reader(f)
    while True:
        #chinese english xxxx key
        row = cf.__next__()
        name = row[3]
        print(name)
        clubdict = want[name] = { 
            'name' : name, 
            'chinese' : row[0],
            'english' : row[1]
        }
        want[latest]['clubs'].append(name)

        #president email blog fb logo xx
        row = cf.__next__()
        clubdict['info'] = [] #new
        info = tsFind(clubdict['info'])
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
            clubdict['logo'] = [] #new
            logo= tsFind(clubdict['logo'])
            logo['src'] = row[4]

        #time\nplace\ntitle\n, .... #for course
        row = cf.__next__()
        clubdict['course'] = [] #new
        course = tsFind(clubdict['course'])
        course['courses'] = []
        for c in row:
            nowc = {}
            c = c.split('\n')
            if len(c) < 2:
                print(c)
                print("course err")
                continue
            if len(c) >= 3:
                nowc['title'] = c[2]
            nowc['time'] = c[0]
            nowc['place'] = c[1]
            course['courses'].append(nowc)
        
        #time\nplace\ntitle\n, .... #for welcome
        #same as above
        row = cf.__next__()
        clubdict['welcome'] = [] #new
        course = tsFind(clubdict['welcome'])
        course['courses'] = []
        for c in row:
            nowc = {}
            c = c.split('\n')
            if len(c) < 2:
                print(c)
                print("course err")
                continue
            if len(c) >= 3:
                nowc['title'] = c[2]
            nowc['time'] = c[0]
            nowc['place'] = c[1]
            course['courses'].append(nowc)

        
        # short_intro course_intro q\na\n... 
        row = cf.__next__()
        clubdict['intro'] = [] #new
        intro = tsFind(clubdict['intro'])
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

        #remove blank content 
        intro['intro'][:] = [ it for it  in intro['intro'] if it['content']]

        #a line for separte each club
        try:
            row = cf.__next__()
        except:
            break;

        #pprint(clubdict)

want[latest]['clubs'].sort()

open("allclubs.json","w").write(json.dumps(want))

