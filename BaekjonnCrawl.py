from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import copy

userURL = 'https://www.acmicpc.net/user/'
problemURL = 'https://www.acmicpc.net/problem/'

try:
    print("Enter user ID")
    name = input(">>")
except TypeError:
    print("Type Error. Write ID with String Type")

userURL = userURL + name

try:
    html = urlopen(userURL)
except HTTPError as e:
    print("HTTP not found. Error Code : 404. Unable to open URL")

try:
    bs = BeautifulSoup(html, 'html.parser')
except URLError as e:
    print("URL Error")

li = bs.find('div',{'class' :'panel-body'}).children#.find('span',{'class' : 'problem_number'})
li = list(li)
for a in range(0,len(li)):
    li[a] = li[a].string

totalProble = []
for b in li:
    totalProble.append(b)

totalProble = list(filter(('\n').__ne__, totalProble))
frameData = pd.DataFrame(columns = ['Question Number','Question Tite','Question URL'])
loopCount = len(totalProble) / 2
varCount = 0
questionCount = 1
while(varCount < loopCount):
    df = pd.DataFrame(data = {'Question Number' : totalProble[varCount],'Question Tite' :totalProble[varCount + 1],'Question URL' : problemURL + str(totalProble[varCount])},
                     index = [questionCount])
    if varCount == 0:
        frameData = df
    else:
        frameData = pd.concat([frameData,df])
    loopCount += 1
    varCount += 2
    questionCount += 1

frameData.to_excel(name + '의 백준 정보' + '.xlsx')