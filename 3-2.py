import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv, datetime

#Australia
ATdict = {}
ATdates = []
ATnums = []
##讀取Australia.csv中的資料
with open('Australia.csv') as f:
    myCsv = csv.reader(f)
    headers = next(myCsv) #headers為第一筆資料:[="2019-06-06", 11,322,315]
    date = ((headers[0]).split('='))[1] #原為="2019-06-06",需去除為"2019-06-06"存入date
    num = headers[1].replace(',', '') #num為電影收益
    ATdict[eval(date)] = int(num) #再將"2019-06-06"去除雙引號,將日期 收益存入ATdict陣列
    ATnums.append(num) #num存入ATnums串列
    #第一筆以後的資料,與上面的處理相同
    for row in myCsv:
        date = ((row[0]).split('='))[1]
        ATdates.append(eval(date))
        num = row[1]
        ATnums.append(num)
ATy = []
#因千位以上的數值有逗號(eg:3,456),需將逗號去除,再存入ATy串列
for i in ATnums:
    b = i.replace(',', '')
    ATy.append(int(b))
#第一筆以後的資料,與上面的處理相同
for i in range(len(ATdates)):
    ATdict[ATdates[i]] = ATy[i]
##將陣列中的日期及數量分別存入串列Atdate及Atnum
ATs = ''
for k, v in ATdict.items():
    ATs += str(k) + ' ' + str(v) + '\n'
ATs = ATs.split('\n')
ATdate = []
ATnum = []
for i in range(len(ATs)-1):
    ATs[i] = ATs[i].split()
    ATnum.append(int(ATs[i][1]))
    ATdate.append(datetime.datetime.strptime(ATs[i][0], '%Y-%m-%d'))

##以下國家皆與澳洲處理相同
#Japan
JPdict = {}
JPdates = []
JPnums = []
with open('Japan.csv') as f:
    myCsv = csv.reader(f)
    headers = next(myCsv)
    date = ((headers[0]).split('='))[1]
    num = headers[1].replace(',', '')
    JPdict[eval(date)] = int(num)
    JPnums.append(num)
    for row in myCsv:
        date = ((row[0]).split('='))[1]
        JPdates.append(eval(date))
        num = row[1]
        JPnums.append(num)
JPy = []
for i in JPnums:
    b = i.replace(',', '')
    JPy.append(int(b))
for i in range(len(JPdates)):
    JPdict[JPdates[i]] = JPy[i]
JPs = ''
for k, v in JPdict.items():
    JPs += str(k) + ' ' + str(v) + '\n'
JPs = JPs.split('\n')
JPdate = []
JPnum = []
for i in range(len(JPs)-1):
    JPs[i] = JPs[i].split()
    JPnum.append(int(JPs[i][1]))
    JPdate.append(datetime.datetime.strptime(JPs[i][0], '%Y-%m-%d'))

#Germany
GMdict = {}
GMdates = []
GMnums = []
with open('Germany.csv') as f:
    myCsv = csv.reader(f)
    headers = next(myCsv)
    date = ((headers[0]).split('='))[1]
    num = headers[1].replace(',', '')
    GMdict[eval(date)] = int(num)
    GMnums.append(num)
    for row in myCsv:
        date = ((row[0]).split('='))[1]
        GMdates.append(eval(date))
        num = row[1]
        GMnums.append(num)
GMy = []
for i in GMnums:
    b = i.replace(',', '')
    GMy.append(int(b))
for i in range(len(GMdates)):
    GMdict[GMdates[i]] = GMy[i]
GMs = ''
for k, v in GMdict.items():
    GMs += str(k) + ' ' + str(v) + '\n'
GMs = GMs.split('\n')
GMdate = []
GMnum = []
for i in range(len(GMs)-1):
    GMs[i] = GMs[i].split()
    GMnum.append(int(GMs[i][1]))
    GMdate.append(datetime.datetime.strptime(GMs[i][0], '%Y-%m-%d'))

#NA
NAdict = {}
NAdates = []
NAnums = []
with open('NorthAmerica.csv') as f:
    myCsv = csv.reader(f)
    headers = next(myCsv)
    date = ((headers[0]).split('='))[1]
    num = headers[1].replace(',', '')
    NAdict[eval(date)] = int(num)
    NAnums.append(num)
    for row in myCsv:
        date = ((row[0]).split('='))[1]
        NAdates.append(eval(date))
        num = row[1]
        NAnums.append(num)
NAy = []
for i in NAnums:
    b = i.replace(',', '')
    NAy.append(int(b))
for i in range(len(NAdates)):
    NAdict[NAdates[i]] = NAy[i]
NAs = ''
for k, v in NAdict.items():
    NAs += str(k) + ' ' + str(v) + '\n'
NAs = NAs.split('\n')
NAdate = []
NAnum = []
for i in range(len(NAs)-1):
    NAs[i] = NAs[i].split()
    NAnum.append(int(NAs[i][1]))
    NAdate.append(datetime.datetime.strptime(NAs[i][0], '%Y-%m-%d'))

###繪圖
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(mdates.YearLocator()) # 設定大刻度
ax.xaxis.set_minor_locator(mdates.MonthLocator()) # 設定小刻度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y')) # 設定大刻度標示
##點上資料
plt.plot(ATdate, ATnum, 'go', label="Australia")
plt.plot(JPdate, JPnum, 'go', color = 'c', label="Japan")
plt.plot(GMdate, GMnum, 'go', color = 'b', label="Germany")
plt.plot(NAdate, NAnum, 'go', color = 'r', label="NorthAmerica")
#繪上圖例
plt.legend(loc="upper right", frameon=False)

plt.show()