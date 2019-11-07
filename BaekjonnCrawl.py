from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import sys

def naviagableStringToNormalString(li,):
    resultList = []
    for navigableSt in li.children:
        resultList.append(navigableSt.string)
    resultList = list(filter(('\n').__ne__, resultList))
    return resultList


def makeDataFrame(li,index):
    frameData = pd.DataFrame(columns=['Question Number', 'Question Tite', 'Question URL'])
    loopCount = len(li) / 2
    varCount = 0
    questionCount = 1
    while (varCount < loopCount):
        df = pd.DataFrame(
            data={'Question Number': li[varCount], 'Question Tite': li[varCount + 1],
                  'Question URL': problemURL + str(li[varCount])},
            index=[questionCount])
        if varCount == 0:
            frameData = df
        else:
            frameData = pd.concat([frameData, df])
        loopCount += 1
        varCount += 2
        questionCount += 1
    if index == 0:
        frameData.to_excel(name + '의 백준 푼문제 리스트' + '.xlsx')
        print("Complete to make Correct question list excel file ( 1 / 2 )")
    elif index == 1:
        frameData.to_excel(name + '의 백준 시도했지만 풀지못한문제 리스트' + '.xlsx')
        print("Complete to make InCorrect question list excel file ( 2 / 2 )")

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



li = bs.findAll('div',{'class' :'panel-body'})[0]#.find('span',{'class' : 'problem_number'})
li2 = bs.findAll('div',{'class' : 'panel-body'})[1]

CorrectIncorrect = []
#맞은문제에 대해

li1StringOnly = naviagableStringToNormalString(li)
CorrectIncorrect.append(li1StringOnly)

#틀린문제에 대해
li2StringOnly = naviagableStringToNormalString(li2)
CorrectIncorrect.append(li2StringOnly)

for cot in range(0, len(CorrectIncorrect)):
    makeDataFrame(CorrectIncorrect[cot],cot)

print('Comlete to make files')
os.system("pause")

