import matplotlib.pyplot as plt
import pandas as pd
import csv
dates = []
nums = []
with open('number_of_films.csv') as f:  #打開number_of_films.csv,並將此命名為f
    myCsv = csv.reader(f)
    headers = next(myCsv)  #headers為第一筆資料:[="2015-01", 694]
    date = ((headers[0]).split('='))[1] #原為="2015-01",需去除為"2015-01"存入date
    num = headers[1] #num為電影數量
    dates.append(eval(date)) #再將"2015-01"去除雙引號,存入dates串列
    nums.append(num) #num存入nums串列
    for row in myCsv: #第一筆以後的資料,與上面的處理相同
        date = ((row[0]).split('='))[1]
        dates.append(eval(date))
        num = row[1]
        nums.append(num)
x = dates
y = []
for i in nums:  #因千位以上的數值有逗號(eg:3,456),需將逗號去除,再存入y串列
    b = i.replace(',', '')
    y.append(int(b))
###繪製圖表
plt.figure(figsize = (80,80)) #視窗大小
plt.bar(x, y) #將x,y資料畫上
plt.gcf().autofmt_xdate() #旋轉x軸標題角度
plt.xticks(fontsize = 8) #設定x軸字體大小
plt.show()

