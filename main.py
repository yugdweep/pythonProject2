from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.ndtv.com/india#pfrom=home-ndtv_mainnavgation'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="news_Itm-cont")

with open('ndtvnews.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    header = ['Title', 'Date', 'Summary']
    csv_writer.writerow(header)

    for list in lists:
        title = list.find('h2', class_="newsHdng").text
        date = list.find('span', class_="posted-by").text
        topic = list.find('p', class_="newsCont").text

        info = [title, date, topic]
        csv_writer.writerow(info)







