from bs4 import BeautifulSoup
import requests
from csv import writer

def ndtv_news(key):

    with open('file1.csv', 'w', newline='') as f:
        csv_writer = writer(f)
        header = ['Title', 'Date', 'Summary']
        csv_writer.writerow(header)

        for i in range(1,6):

            url = "https://www.ndtv.com/india/page-" + str(i)

            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            lists = soup.find_all('div', class_="news_Itm-cont")

            news_list = []

            for list in lists:
                news_title = list.find('h2', class_="newsHdng")
                date = list.find('span', class_="posted-by").text.strip()
                topic = list.find('p', class_="newsCont").text.strip()

                # checking for duplicates
                if news_title not in news_list:
                    if date not in news_list:
                        if topic not in news_list:
                            news_list.append(news_title)
                        news_list.append(date)
                    news_list.append(topic)

                info = [news_title, date, topic]
                csv_writer.writerow(info)
            print(news_list)

ndtv_news(1)
