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

## Project Command line
### Init
```
yarn global add @vue/cli
vue create
```

### Setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production

```
yarn build
cp dist path_your_static_server
```

If not work(Vue-router is annoying), build development version.
```
yarn build -m develop
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
