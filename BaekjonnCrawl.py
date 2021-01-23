import os
try:
    from urllib.request import URLError
    from urllib.request import HTTPError
    from urllib.request import urlopen,quote
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import sys
    import time
    import warnings
    warnings.filterwarnings(action='ignore')

    now = time.localtime()
    # 기존 데이터 존재여부
    before_data_exist = False
    # 기존 데이터가 있던 경우에 새로 푼 문제들정보
    new_solved = []
    # 기존데이터가 있던 경우 기존데이터대입
    prev_data = None


    def naviagableStringToNormalString(li, ):
        resultList = []
        for navigableSt in li.children:
            resultList.append(navigableSt.string)
        resultList = list(filter(('\n').__ne__, resultList))
        return resultList

    def getQID(qNumber):
        html = BeautifulSoup(urlopen('https://www.acmicpc.net/problem/' + qNumber))
        return html.find('span',{'id' : 'problem_title'}).text

    def makeDataFrame(li, index):
        frameData = pd.DataFrame(columns=['Question Number', 'Question Tite', 'Question URL', 'Updated Time'])
        loopCount = len(li)
        varCount = 0
        questionCount = 1 #질문번호 Index
        while (varCount < loopCount):
            df = pd.DataFrame(
                data={'Question Number': li[varCount], 'Question Title': getQID(li[varCount]),
                      'Question URL': problemURL + str(li[varCount]),
                      'Updated Time': "%04d-%02d-%02d %02d:%02d:%02d" % (
                      now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)},
                index=[questionCount])
            if varCount == 0:
                frameData = df
            else:
                frameData = pd.concat([frameData, df])
            varCount += 1
            questionCount += 1
        if index == 0:
            frameData.to_excel(name + '의 백준 푼문제 리스트' + '.xlsx')
            print("Complete to make Correct question list excel file ( 1 / 2 )")
        elif index == 1:
            frameData.to_excel(name + '의 백준 시도했지만 풀지못한문제 리스트' + '.xlsx')
            print("Complete to make InCorrect question list excel file ( 2 / 2 )")    
        
        
        
    def add_New(li): # 여기 넘어오는 li는 새로 추가된 데이터들에 대한 데이터만 들어온다.
        frameData = pd.DataFrame(columns=['Question Number', 'Question Tite', 'Question URL', 'Updated Time'])
        loopCount = len(li)
        varCount = 0
        questionCount = list(prev_data.index)[-1] + 1
        while varCount < loopCount:
            df = pd.DataFrame(
                data={'Question Number': li[varCount], 'Question Title': getQID(li[varCount]),
                      'Question URL': problemURL + str(li[varCount]),
                      'Updated Time': "%04d-%02d-%02d %02d:%02d:%02d" % (
                      now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)},
                index=[questionCount])
            if varCount == 0:
                frameData = df
            else:
                frameData = pd.concat([frameData, df])
            varCount += 1
            questionCount += 1 
        
        new_sync_data = pd.concat([prev_data, frameData])
        new_sync_data.to_excel(name + '의 백준 푼문제 리스트' + '.xlsx')
        print("Complete to make Correct question list excel file ( 1 / 2 )")
    
    def initiateGlobalDatas():
        now = time.localtime()
        before_data_exist = False
        new_solved = []
        prev_data = None
        
    loop = True
    while loop:
        userURL = 'https://www.acmicpc.net/user/'
        problemURL = 'https://www.acmicpc.net/problem/'
        print("Enter user ID")
        name = quote(input(">>"))
        userURL = userURL + name
        html = urlopen(userURL)
        bs = BeautifulSoup(html, 'html.parser')

        li = bs.findAll('div', {'class': 'panel-body'})[0]  # .find('span',{'class' : 'problem_number'})
        li2 = bs.findAll('div', {'class': 'panel-body'})[1]
        
        
        CorrectIncorrect = []
        # 맞은문제에 대해
        li1StringOnly = naviagableStringToNormalString(li)
        CorrectIncorrect.append(li1StringOnly)

        # 틀린문제에 대해
        li2StringOnly = naviagableStringToNormalString(li2)
        CorrectIncorrect.append(li2StringOnly)
        

        program_dir = os.getcwd()
        xl_list = os.listdir(program_dir)
        # 확장자가 .xlsx(Microsoft Excel File)인 파일들만 리스트로 출력해서 파일 확인하기
        xl_list = [file for file in xl_list if file.endswith("의 백준 푼문제 리스트.xlsx")]
        for t in range(0, len(xl_list)):
            if name == xl_list[t].split(' ')[0].split('의')[0]:
                before_data_exist = True
                prev_data = pd.read_excel(name + '의 백준 푼문제 리스트' + '.xlsx', index_col=0,engine='openpyxl')
                prev_data_Qlist = list(prev_data['Question Number'])
                new_solved = list(filter(lambda x: int(x) not in prev_data_Qlist, CorrectIncorrect[0]))
                del CorrectIncorrect[0]
                CorrectIncorrect.insert(0, new_solved)
                break
            else:
                continue

        for cot in range(0, len(CorrectIncorrect)):
            if cot == 0 and before_data_exist == True:
                add_New(CorrectIncorrect[cot])
            else:
                makeDataFrame(CorrectIncorrect[cot], cot)

        print('Comlete to make files')
        print("Would you like to go on? (Y / N)")
        cp = input(">>")
        if cp == 'y' or cp == 'Y':
            os.system('cls')
            initiateGlobalDatas()
            time.sleep(0.5)
        elif cp == 'N' or cp == 'n':
            loop = False
        else:
            loop = False
except TypeError:
    print("Type Error Occured.")
    os.system("pause")
except HTTPError as e:
    print(e)
    os.system("pause")
except URLError as e:
    print(e)
    os.system("pause")
except PermissionError as e:
    print("Permission Error : Please check if selected file has been opened.")
    os.system("pause")
except ImportError as e:
    print("Module or Package import has been crushed! Please contact to developer.")
    os.system("pause")
