import random

allclubs =['太極拳研究社', '少林拳社', '國術社', '國術校隊', '楊氏廣法太極拳社', '八步螳螂拳社', '綜合格鬥社', '合氣太極社', '內家武學社', '跆拳道社', '劍道社', '楊太極武藝社', '椰林合氣道社', '居合道社', '截拳道社', '技擊散打社', '空手道社', '詠春拳社', '柔道社'] 

pic_clubs = []

nopic_clubs = ['少林拳社', '居合道社', '合氣太極社', '椰林合氣道社', '柔道社', '詠春拳社', '國術校隊', '跆拳道社', '楊太極武藝社', '綜合格鬥社']

for c in allclubs:
    if c not in nopic_clubs:
        pic_clubs.append(c)

random.shuffle(pic_clubs)
random.shuffle(nopic_clubs)

rank = len(allclubs)

for c in nopic_clubs:
    print(rank,end=' -> ')
    print(c)
    rank-=1

print('---')

for c in pic_clubs:
    print(rank,end=' -> ')
    print(c)
    rank-=1


