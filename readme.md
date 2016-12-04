# NTUMU_web

NTU Marital Art Union

## The page

homepage.ntu.edu.tw/~b04611017/


# build data from csv

transfer your csv data to json by python

## build

` python3 dataTojson.py build `

## update club

` python3 dataTojson.py clubUpdate yourcsv.csv `

## update common thing 

like. boothmap, countdown, showtime

` python3 dataTojson.py commonUpdate yourcsv.csv `

all the format spec are written in dataTojson.py

and the output is allclubs.json


# build the web

I use [vue-cli](https://github.com/vuejs/vue-cli) [vue-router](https://github.com/vuejs/vue-router) to do that

build : ` npm init `

run   : ` npm run dev `

build : ` npm run build `

# put your asset

```
favicon.ico
static
├ logo 
├   └ xxx.png
└── img
    ├── 105_1_logo.png
    ├── clublogo
    │   └── 105_1_logo_*.png
    ├── countdown
    │   ├── 105_1_count*_*.jpg
    │   └── 105_1_count*_*_full.jpg
    ├── permanent_logo.png
    └── permanent_logo_small.png

src/assets
└── allclubs.json
```
Remind : the picture **should** shrink 

You can use [https://tinypng.com/](https://tinypng.com/)

Remember to put .ico in root


