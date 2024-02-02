import requests, csv, calendar
from bs4 import BeautifulSoup
this = []
###2019年6月~12月
for month1 in range(6, 13):
    #若月份小於10,需在首補0(eg:01,02...,10,11,12)
    if (month1//10)==0: 
        a = '0' + str(month1)
    else:
        a = str(month1)
    #將月份填入網址
    url = 'https://www.boxofficemojo.com/calendar/2019-' + a + '-01/' 
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    #擷取電影清單頁面下各個電影資訊的連結
    href = bs.select('a[href]')
    a = []
    c = []
    for k in href: 
        a.append(k.get('href'))
    for i in range(4, len(a)):
        b = a[i].split('/')
        if (b[1] == 'release') and (a[i] not in c): 
            c.append(a[i])
    #擷取各個電影資訊的日期及數量
    for i in c:
        num = 0
        urll = 'https://www.boxofficemojo.com/' + i
        htmll = requests.get(urll)
        bss = BeautifulSoup(htmll.text, 'html.parser')
        a = bss.find_all('div',{'class':'a-section a-spacing-none'})
        for j in range(len(a)):
            aa = a[j].text.split()
            #擷取Release欄位存入c
            if aa[0] == 'Release': 
                b = a[j].text
                date = (b[12:].split(','))[0]
                c = date
                if date[:2].isspace():
                    c = (date.split(')'))[1]
            #擷取Widest欄位存入num
            if aa[0] == 'Widest': 
                b = a[j].text.split()
                num = int(((b[1])[7:]).replace(',', ''))
        aaa = c.split()
        #將月份由英文轉為數字形式
        month = list(calendar.month_abbr).index(aaa[0])
        #只擷取6~12月,其他略過 
        if month != month1:
            continue 
        else:
            #若月份小於10,需在首補0(eg:01,02...,10,11,12)
            if (int(month)//10)==0: 
                months = '0' + str(month)
            else:
                months = str(month)
            #若天數小於10,需在首補0(eg:01,02...,10,11,12...)
            if (int(aaa[1])//10)==0: 
                days = '0' + str(aaa[1])
            else:
                days = str(aaa[1])
            #final為2019-月份-天數
            final = '2019-' + str(months) + '-' + str(days) 
            #將[日期, 數量]存入this串列
            this.append([final, num]) 
   
###2020年1月~5月  
#以下處理皆與上述相同        
for month1 in range(1, 6):
    if (month1//10)==0:
        a = '0' + str(month1)
    else:
        a = str(month1)
    url = 'https://www.boxofficemojo.com/calendar/2020-' + a + '-01/' 
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    href = bs.select('a[href]')
    a = []
    c = []
    for k in href:
        a.append(k.get('href'))
    for i in range(4, len(a)):
        b = a[i].split('/')
        if (b[1] == 'release') and (a[i] not in c): 
            c.append(a[i])
    for i in c:
        num = 0
        urll = 'https://www.boxofficemojo.com/' + i
        htmll = requests.get(urll)
        bss = BeautifulSoup(htmll.text, 'html.parser')
        a = bss.find_all('div',{'class':'a-section a-spacing-none'})
        for j in range(len(a)):
            aa = a[j].text.split()
            if aa[0] == 'Release':
                b = a[j].text
                date = (b[12:].split(','))[0]
                c = date
                if date[:2].isspace():
                    c = (date.split(')'))[1]
            if aa[0] == 'Widest':
                b = a[j].text.split()
                num = int(((b[1])[7:]).replace(',', ''))
        aaa = c.split()
        month = list(calendar.month_abbr).index(aaa[0])
        if month1 != month:
            continue
        else:
            if (int(month)//10)==0:
                months = '0' + str(month)
            else:
                months = str(month)
            if (int(aaa[1])//10)==0:
                days = '0' + str(aaa[1])
            else:
                days = str(aaa[1])
            final = '2020-' + str(months) + '-' + str(days)
            this.append([final, num])
###將擷取的將擷取的資料以"日期 數量"格式寫入csv檔中        
with open('theaters.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in this:
        writer.writerow(['="{}"'.format(i[0]), i[1]])