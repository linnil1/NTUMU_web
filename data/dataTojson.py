import json
import csv
import sys
import os.path
from pprint import pprint
import markdown2 

"""
#Wanted clubs data 
#JSON format
{
    latest: "105_1",
    "105_1":{ #version
        clubs : [""], #clubs name
        logo: "", 
        showtime:{
            title: 2015/12/4,
            desp: where is the stage,
            shows:[ {time,clubname,title},... ]  
        }
        countdown:{
            title: the show is waiting for you,
            desp: 
            counts:[ {name,title,src,fullsrc,desp},...]
        }
        boothmap : {
            lat: 
            log:
            zoom:
            maps:[{name,lon,lat,num},...]}
    },

    "YangTai": { #clubs name
        name : "YangTai", #same as key
        chinese: "",
        english: "",
        logo: src ,  #newest logo 
        latest: "105_1", 
        105_1:{
            logo : src,
            chinese: "",
            english: "",
            course:[
                { title,time,place}  #course data
            ],
            welcome: [{}], #same as course
            info: {
                president: "范思晴",
                email : "taida.taichi@gmail.com",
                blog : "taida-taichi.blogspot.com",
                fb : {
                        name : "台大太極拳社 NTU Taichi Club",
                        link : "https://www.facebook.com/4/"
                },
            },
            intro: [{
                id: "qa",  ## qa is be special parsed
                name: "Q-A",
                content:[{
                    q: "question？",
                    a: "answer。"
			}
                    ]
                },
                {id,name,content} # otherwise content should be html
            ]
        }
    }
}
"""

def markdown(data):
    return markdown2.markdown(data, extras=["tables","cuddled-lists"])


def clubUpdate(ts,filename):
    """ Parse club data csv to json format file """

    # open data or open blank data
    if os.path.isfile("./allclubs.json"):
        want = json.load(open("./allclubs.json"))
    else:
        want = {'latest':ts}

    # Overwrite data if exist
    want['latest'] = max(want['latest'], ts)
    want[ts] = want.get(ts,{})
    want[ts]['clubs'] = []

    """ csv data
chinese english xxxx name
president email blog fb logo xx
time\nplace\ntitle\n, .... #for course
time\nplace\ntitle\n, .... #for welcome
short_intro course_intro q\na\n ... (title content)
a line for separte each club
    """
    with open(filename,newline='') as f:
        cf = csv.reader(f)
        #Ignore Header
        for i in range(6):
            next(cf)

        #Each club
        while True:
            # First Line 
            # chinese english xxxx name
            row = next(cf)
            name = row[3].strip()
            print("Now Parsing :" + name)
            want[name] = want.get(name, {})
            want[ts]['clubs'].append(name)
            base_data = { 
                    'name': name, 
                    'chinese': row[0].strip(),
                    'english': row[1].strip(),
                    'latest': ts
                }
            # update if it is newest data
            if not want[name].get("latest") or want[name]["latest"] <= ts:
                want[name].update(base_data)

            want[name]['version'] = want[name].get('version',[])
            if ts not in want[name]['version']:
                want[name]['version'].append(ts)
                want[name]['version'].sort() 
            clubdict = want[name][ts] = dict(base_data) #copy

            # Second Line 
            # president email blog fb logo xx
            row = next(cf)
            info = clubdict['info'] = {
                    'president' : row[0].strip(),
                    'email' : row[1].strip(),
                    'blog' : row[2].strip(),
                    'fb': {},
            }
            if row[3]: #fb
                line = row[3].strip().split('\n')
                info['fb']['name'] = line[0].strip()
                if len(line) > 1:
                    info['fb']['link'] = line[1].strip()
            if row[4]: #logo
                clubdict['logo'] = row[4].strip()
                if want[name]['latest'] <= ts:
                    want[name]['logo'] = clubdict['logo']

            # Third Line 
            # time\nplace\ntitle\n, .... #for course
            def courseRead(course_name):
                row = next(cf)
                course = clubdict[course_name] = []
                for c in row:
                    c = list(filter(lambda a:a.strip(), c.strip().split('\n')))
                    if not c: #empty
                        continue
                    if len(c) < 2:
                        print("Wrong : " + str(c))
                        continue
                    nowc = {}
                    nowc['time'] = c[0].strip()
                    nowc['place'] = c[1].strip()
                    if len(c) >= 3 and c[2].strip():
                        nowc['title'] = c[2].strip()
                    course.append(nowc)
            courseRead("course")
            courseRead("welcome")
            
            # Fourth Line 
            # short_intro course_intro q\na\n... 
            rows = next(cf)
            intro = clubdict['intro'] = []
            for row in rows:
                row = row.strip()
                if not row:
                    continue;
                rowtitle = row.split("\n")[0].strip()
                if rowtitle == "QA": # QA
                    qas = list(filter(None,row.split('\n')[1:]))
                    qalist = []
                    for line in range(0,len(qas),2):
                        qalist.append({ #remove Q A
                            'q':qas[line][1:],
                            'a':qas[line+1][1:]
                        })
                    intro.append({
                        'id' : "qa",
                        'name' : "Q-A",
                        'content' : qalist
                    })
                    continue
                intro.append({
                    'id' : rowtitle,
                    'name' : rowtitle,
                    'content' : markdown(row[row.find('\n')+1:])
                })

            # Blank Line for separation
            try:
                next(cf)
            except:
                break;

            #pprint(clubdict)

    want[ts]['clubs'].sort()
    json.dump(want, open("./allclubs.json","w"))


def commonUpdate(ts,filename):
    # open data or open blank data
    if os.path.isfile("./allclubs.json"):
        want = json.load(open("./allclubs.json"))
    else:
        want = {'latest':ts, ts:{}}

    """ 
csv data
showtime title desp
name title src desp
...

booth lat lon zoom
name lonlat number
...

countdown title desp
name title src fullsrc desp
...
    """
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

        print("showtime")
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

        print("map")
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
        
        print("countdown")
        want[ts]['countdown'] = {
                'title' : data['countdown'][0][1],
                'desp' : data['countdown'][0][2],
                'counts' : []
        }
        for count in data['countdown'][1:]:
            want[ts]['countdown']['counts'].append({
                'name': count[0],
                'title': count[1],
                'src' : count[2],
                'fullsrc' : count[3],
                'desp': markdown(count[4])
            })
    
    want[ts]['logo'] = ts+"_logo.png"
    json.dump(want, open("./allclubs.json","w"))

def checkPrint(): 
    want = json.load(open("./allclubs.json"))
    pprint(want['YangTai'])
    pprint(want['105_1'])

clubUpdate("105_10","105_1_club.csv")
commonUpdate("105_10","105_1_common.csv")
checkPrint()

