from bs4 import BeautifulSoup
import requests
from csv import writer

with open('ntdvnewsyug.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    header = ['Title', 'Date', 'Summary']
    csv_writer.writerow(header)

    for i in range(1,11):
        url = "https://www.ndtv.com/india/page-"+str(i)

        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        lists = soup.find_all('div', class_="news_Itm-cont")

        for list in lists:
            title = list.find('h2', class_="newsHdng").text.strip()
            date = list.find('span', class_="posted-by").text.strip()
            topic = list.find('p', class_="newsCont").text.strip()

            info = [title, date, topic]
            csv_writer.writerow(info)
            print(info)










