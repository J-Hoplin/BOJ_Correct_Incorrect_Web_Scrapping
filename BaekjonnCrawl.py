from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import sys

userURL = 'https://www.acmicpc.net/user/'
problemURL = 'https://www.acmicpc.net/problem/'

try:
    print("Enter user ID")
    name = input(">>")
except TypeError:
    print("Type Error. Write ID with String Type")
    sys.exit()

userURL = userURL + name

try:
    html = urlopen(userURL)
except HTTPError as e:
    print(e)
    sys.exit()

try:
    bs = BeautifulSoup(html, 'html.parser')
except URLError as e:
    print(e)
    sys.exit()

li = bs.find('div',{'class' :'panel-body'}).children#.find('span',{'class' : 'problem_number'})
li = list(li)
totalProble = []
for a in range(0,len(li)):
    li[a] = li[a].string
    totalProble.append(li[a])


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
print("Complete to make file")
os.system("pause")
