# NTUMU_web

NTU Marital Art Union

## The page

homepage.ntu.edu.tw/~b04611017/


# build data from csv to json

transfer your csv data to json by python3

put your csv in `./data/` with name 
`xxxxx_club.csv`(for club data) or 
`xxxxx_common.csv`(for boothmap, countdown showtime data)

`xxxxx` is version number. Like: `105_1`

and Run 

```
pip3 install markdown2 --user
python3 data/dataTojson.py
```

all the format spec are written in dataTojson.py

# build the static web

I use 
[vue-cli](https://github.com/vuejs/vue-cli) 
[vue-router](https://github.com/vuejs/vue-router) to do that

## put your asset like below

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
```
Remind : the picture **should** shrink 

You can use [https://tinypng.com/](https://tinypng.com/)

Remember to put .ico in root

## build it

init : ` npm install`

build : ` npm run build `

You can also run ` npm run dev ` to see if it is ok

After build it, all files are in `dist/`

and upload to your server

