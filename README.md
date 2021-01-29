BOJ Correct Incorrect Crawl
===
***

- What for? : [백준 온라인저지](https://www.acmicpc.net/)에서 사용자가 맞은 문제들과 틀린문제들의 리스트를  엑셀로 출력해주는 프로그램입니다.

- Language : Python 3.7

- ENV : JetBrain Pycharm, Windows 10

- Used Modules : pandas, bs4, urllib, pyinstaller(to make exe file)

- Install requirements

    ~~~
    pip3 install -r requirements.txt
    ~~~

- pyinstaller command to make exe : pyinstaller -F BaekjonnCrawl.py -n BaekjonnCrawl.py

***

- 2019/11/20

    - Make time sync columns : The most recent crawl date is now entered.

    - Now, if you have data for an existing user, it's not about creating new data and replacing it, but rather merging data that's not there compared to the existing data. This is to counteract the 'Updated Time' column.

- 2019/12/03

    - Enable Loop
    - Re : Exception Handling - handle permission error

***

### How to Use?

- First when you open the program CLI will open like this.

    
    ![img](BOJimg/1.PNG)


- Next enter your Baekjoon Online judge's ID(Nickname).


- When you enter your name properly excel files will be generated in directory of this program.


   ![img](BOJimg/2.PNG)
