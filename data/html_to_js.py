from lxml import html
import os
import re

def bracketMatch(text):
    if text[0]=='{' :
        want = '}'
    elif text[0]=='(' :
        want = ')'
    else:
        want = text[0]
    index = 1
    while index < len(text) :
        #print(text[index])
        if text[index] == want:
            return index
        elif text[index] == '\\':
            index+=1
        elif want in "'\"":
            index+=1
            continue
        elif  text[index] in "'\"({" :
            index += bracketMatch(text[index:])
        elif text[index] == '/':
            if text[index+1] ==  '/' : # comment
                index += text[index:].find("\n")
            elif text[index+1] ==  '*' : # multi comment
                index += text[index:].find("*/")+1
            else:
                raise "error"
        index+=1

fs = os.listdir(".")

fs = [ f for f in fs if f.startswith("json_") and f.endswith(".html")]

"""
style should put inside the key div
script should put at the last 
"""

allstr = ""
for f in fs:
    word = re.findall(r"json_(.*)\.html",f)[0]
    print(word)
    fhtml = html.fromstring(open(f).read())
    goal_html = fhtml.xpath("//*[@id='"+word+"']")[0]
    html_str = "var "+word+"_html = "+repr(html.tostring(goal_html).decode("utf8"))

    #print(goalstr)

    jsstr = fhtml.xpath("//script")[-1].text
    while True:
        jsstr = jsstr[jsstr.find("Vue"):]
        jsstr = jsstr[jsstr.find("{"):]

        strend = bracketMatch(jsstr)+1

        print(word)
        print(strend)

        goal_vue = jsstr[:strend]
        if "#navbar" in goal_vue :
            continue;
        else:
            vue_str = "var "+word+"_vue = "+goal_vue
            break;

    allstr += html_str + "\n"
    allstr += vue_str + "\n"


open("all.js","w").write(allstr)



