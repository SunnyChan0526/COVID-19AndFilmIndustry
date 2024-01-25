import requests, csv, datetime
from bs4 import BeautifulSoup
with open('number_of_films.csv', 'w', newline='') as csvfile: #建立檔名為number_of_films.csv的檔案,並將此命名為csvfile
    writer = csv.writer(csvfile)
    for i in range(2015, 2021):  #i為年分
        for j in range(1, 13):   #j為月份
            if (j//10)==0:       #若j月份小於10,需在首補0(eg:01,02...,10,11,12)
                a = '0' + str(j) 
            else:
                a = str(j)
            url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=' + str(i) + '-' + a + '-01,' + str(i) + '-' + a + '-31' #將月份填入網址
            html = requests.get(url)
            bs = BeautifulSoup(html.text, 'html.parser')

            date = bs.select(".header")
            aa = date[0].text.split()
            date = datetime.date.fromisoformat(aa[4])
            date = date.strftime("%Y-%m")

            num = bs.select(".desc") 
            nums = num[0].text
            ans = nums.split()
            writer.writerow(['="{}"'.format(date), ans[2]]) #以2015-01 600的格式寫入csv檔