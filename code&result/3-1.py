import calendar
import requests, csv
from bs4 import BeautifulSoup
###Australia
#2019年6月~12月
url = 'https://www.boxofficemojo.com/weekend/by-year/2019/?area=AU'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
date = bs.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bs.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
ans = []
for i in range(len(date)):
    a = date[i].text.split()
    #日期編排由大到小,因此到5月即結束
    if a[0] == 'May': 
        break
    else:
        #將月份由英文轉為數字形式
        month = list(calendar.month_abbr).index(a[0]) 
        b = a[1].split('-')
        #若月份小於10,需在首補0(eg:01,02...,10,11,12)
        if (month//10)==0: 
            months = '0' + str(month)
        else:
            months = str(month)
        #若天數小於10,需在首補0(eg:01,02...,10,11,12...)
        if (int(b[0])//10)==0: 
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        #將$去除
        moneyy = money[i].text.split('$') 
        this = str(moneyy[1])
        #a為2019-月份-天數
        a = str('2019-' + months + '-' + day) 
        ans.append([a, this])  
#2020年1月~5月
urll = 'https://www.boxofficemojo.com/weekend/by-year/2020/?area=AU'
htmll = requests.get(urll)
bss = BeautifulSoup(htmll.text, 'html.parser')
date = bss.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bss.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
anss = []
for i in range(len(date)):
    a = date[i].text.split()
    #日期編排由大到小,因此至5月以前都是略過(寫時為6月,因此還未有7月資料)
    if a[0] == 'Jun': 
        continue
    #以下處理皆與上述相同
    else: 
        month = list(calendar.month_abbr).index(a[0])
        b = a[1].split('-')
        if (month//10)==0:
            months = '0' + str(month)
        else:
            months = str(month)
        if (int(b[0])//10)==0:
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        moneyy = money[i].text.split('$')
        this = str(moneyy[1])
        a = str('2020-' + months + '-' + day)
        anss.append([a, this])
#2019資料由原本編排時間由大到小轉為小到大(eg:12,11,10 => 10,11,12)
ans.reverse() 
#2020資料,,
anss.reverse()
a = ans + anss
##將資料寫入Australia.csv
with open('Australia.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(a)):
        date = a[i][0]
        money = a[i][1]
        writer.writerow(['="{}"'.format(date), money])
###以下國家皆與上述處理相同
###Japan
url = 'https://www.boxofficemojo.com/weekend/by-year/2019/?area=JP'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
date = bs.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bs.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
ans = []
for i in range(len(date)):
    a = date[i].text.split()
    if a[0] == 'May':
        break
    else:
        month = list(calendar.month_abbr).index(a[0])
        b = a[1].split('-')
        if (month//10)==0:
                    months = '0' + str(month)
        else:
            months = str(month)
        if (int(b[0])//10)==0:
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        moneyy = money[i].text.split('$')
        this = str(moneyy[1])
        a = str('2019-' + months + '-' + day)
        ans.append([a, this])

urll = 'https://www.boxofficemojo.com/weekend/by-year/2020/?area=JP'
htmll = requests.get(urll)
bss = BeautifulSoup(htmll.text, 'html.parser')
date = bss.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bss.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
anss = []
for i in range(len(date)):
    a = date[i].text.split()
    if a[0] == 'Jun':
        continue
    else:
        month = list(calendar.month_abbr).index(a[0])
        b = a[1].split('-')
        if (month//10)==0:
            months = '0' + str(month)
        else:
            months = str(month)
        if (int(b[0])//10)==0:
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        moneyy = money[i].text.split('$')
        this = str(moneyy[1])
        a = str('2020-' + months + '-' + day)
        anss.append([a, this])
ans.reverse()
anss.reverse()
a = ans + anss

with open('Japan.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(a)):
        date = a[i][0]
        money = a[i][1]
        writer.writerow(['="{}"'.format(date), money])
    
###Germany
url = 'https://www.boxofficemojo.com/weekend/by-year/2019/?area=DE'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
date = bs.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bs.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
ans = []
for i in range(len(date)):
    a = date[i].text.split()
    if a[0] == 'May':
        break
    else:
        month = list(calendar.month_abbr).index(a[0])
        b = a[1].split('-')
        if (month//10)==0:
                    months = '0' + str(month)
        else:
            months = str(month)
        if (int(b[0])//10)==0:
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        moneyy = money[i].text.split('$')
        this = str(moneyy[1])
        a = str('2019-' + months + '-' + day)
        ans.append([a, this])

urll = 'https://www.boxofficemojo.com/weekend/by-year/2020/?area=DE'
htmll = requests.get(urll)
bss = BeautifulSoup(htmll.text, 'html.parser')
date = bss.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bss.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
anss = []
for i in range(len(date)):
    a = date[i].text.split()
    if a[0] == 'Jun':
        continue
    else:
        month = list(calendar.month_abbr).index(a[0])
        b = a[1].split('-')
        if (month//10)==0:
            months = '0' + str(month)
        else:
            months = str(month)
        if (int(b[0])//10)==0:
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        moneyy = money[i].text.split('$')
        this = str(moneyy[1])
        a = str('2020-' + months + '-' + day)
        anss.append([a, this])
ans.reverse()
anss.reverse()
a = ans + anss

with open('Germany.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(a)):
        date = a[i][0]
        money = a[i][1]
        writer.writerow(['="{}"'.format(date), money])

###NorthAmerica
url = 'https://www.boxofficemojo.com/weekend/by-year/2019/'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
date = bs.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bs.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
ans = []
for i in range(len(date)):
    a = date[i].text.split()
    if a[0] == 'May':
        break
    else:
        month = list(calendar.month_abbr).index(a[0])
        b = a[1].split('-')
        if (month//10)==0:
                    months = '0' + str(month)
        else:
            months = str(month)
        if (int(b[0])//10)==0:
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        moneyy = money[i].text.split('$')
        this = str(moneyy[1])
        a = str('2019-' + months + '-' + day)
        ans.append([a, this])

urll = 'https://www.boxofficemojo.com/weekend/by-year/2020/'
htmll = requests.get(urll)
bss = BeautifulSoup(htmll.text, 'html.parser')
date = bss.find_all('td', {'class':'a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column'})
money = bss.find_all('td', {'class':'a-text-right mojo-field-type-money mojo-estimatable'})
anss = []
for i in range(len(date)):
    a = date[i].text.split()
    if a[0] == 'Jun':
        continue
    else:
        month = list(calendar.month_abbr).index(a[0])
        b = a[1].split('-')
        if (month//10)==0:
            months = '0' + str(month)
        else:
            months = str(month)
        if (int(b[0])//10)==0:
            day = '0' + str(b[0])
        else:
            day = str(b[0])
        moneyy = money[i].text.split('$')
        this = str(moneyy[1])
        a = str('2020-' + months + '-' + day)
        anss.append([a, this])
ans.reverse()
anss.reverse()
a = ans + anss
with open('NorthAmerica.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(a)):
        date = a[i][0]
        money = a[i][1]
        writer.writerow(['="{}"'.format(date), money])
