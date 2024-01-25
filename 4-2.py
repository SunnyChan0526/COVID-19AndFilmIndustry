import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv, datetime

dicts2019 = {}
dicts2020 = {}
nums = []
###將theaters.csv檔的資料,以"'月分':[數量串列]"存入dicts2019及dicts2020陣列中
with open('theaters.csv') as f:
    myCsv = csv.reader(f)
    headers = next(myCsv)
    month = ((((headers[0]).split('='))[1]).split('-'))[1]
    num = int(headers[1].replace(',', ''))
    dicts2019[month] = []
    dicts2019[month].append(num)
    for row in myCsv:
        year = ((((row[0]).split('='))[1]).split('-'))[0]
        month = ((((row[0]).split('='))[1]).split('-'))[1]
        num = int(row[1])
        if month not in dicts2019:
            dicts2019[month] = []
        if month not in dicts2020:
            dicts2020[month] = []
        if year == '"2019':
            dicts2019[month].append(num)
        if year == '"2020':
            dicts2020[month].append(num)
num2019 = {}
for i in dicts2019:
    #2019 1~5月為None
    if dicts2019[i] is not None: 
        num2019[i] = {}
        for j in dicts2019[i]:
            #1000為一個維度,計算該數字屬於哪一區間(0~1000:一區間;1000~2000:二區間;......)
            x = (int(j)//1000) + 1 
            #將各區間資料陣列存入月份陣列中(eg:{'06':{1:6442, 5:13363}, '07':{1:10163, 5:9436}})
            if x not in num2019[i]:
                num2019[i][x] = j
            else:
                num2019[i][x] += j
num2020 = {}
for i in dicts2020:
    #2020 6~12月為None
    if dicts2020[i] is not None:
        #與num2019處理相同
        num2020[i] = {}
        for j in dicts2020[i]:
            x = (int(j)//1000) + 1
            if x not in num2020 [i]:
                num2020[i][x] = j
            else:
                num2020[i][x] += j
###繪熱區圖
final = []
##去除num2019及num2020陣列中的月份
num2019.pop('01')
num2019.pop('02')
num2019.pop('03')
num2019.pop('04')
num2019.pop('05')
num2020.pop('06')
num2020.pop('07')
num2020.pop('08')
num2020.pop('09')
num2020.pop('10')
num2020.pop('11')
num2020.pop('12')
##圖表由左而右,由上到下排列數值,存入串列中(一列為一組串列)
for i in range(5, 0, -1):
    lists = []
    for j in num2019:
        if i in num2019[j]:
            lists.append(int(num2019[j][i]))
        else:
            lists.append(0)
    for j in num2020:
        if i in num2020[j]:
            lists.append(int(num2020[j][i]))
        else:
            lists.append(0)
    final.append(lists)

month = []
##若月份小於10,需在首補0(eg:01,02...,10,11,12)
for j in range(6, 13):
    if (j//10)==0:
        a = '0' + str(j)
        month.append(a)
    else:
        a = str(j)
        month.append(a)
for j in range(1, 6):
    if (j//10)==0:
        a = '0' + str(j)
        month.append(a)
    else:
        a = str(j)
        month.append(a)
#第0及7位置要出現年分
month[0] = '2019-06'
month[7] = '2020-01'


num = ['5000', '4000', '3000', '2000', '1000']
date = month

harvest = np.array(final)


fig, ax = plt.subplots()
im = ax.imshow(harvest)

##設定x,y軸範圍
ax.set_xticks(np.arange(len(date)))
ax.set_yticks(np.arange(len(num)))
##設定x,y軸標籤
ax.set_xticklabels(date)
ax.set_yticklabels(num)
#旋轉x軸標籤並設定對其方式:anchor
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

##繪上x,y軸標籤
for i in range(len(num)):
    for j in range(len(date)):
        text = ax.text(j, i, harvest[i, j], ha="center", va="center", color="w")
#繪上標題
ax.set_title("theaters")
fig.tight_layout()
plt.show()







