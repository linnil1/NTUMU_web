#NTUMU_web

## NTU Marital Art Union

## The page is on homepage.ntu.edu.tw/~b04611017/


# Usage

transfer your csv data to json by python

### build

` python3 dataTojson.py build `

### update club

` python3 dataTojson.py clubUpdate yourcsv.csv `

### update common thing 

like. boothmap, countdown, showtime

` python3 dataTojson.py commonUpdate yourcsv.csv `

all the format spec are written in dataTojson.py

and the output is allclubs.json


# build the web

I use ugly methods to do that

put your html in data/ and add prefix json_

run `python3 html_to_js.py` will put it all into all.js

you should mind the keyword in your json_*.html file



