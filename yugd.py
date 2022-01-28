from bs4 import BeautifulSoup
import requests
# from csv import writer
import time

print('new links are in search enter 1')
l  = input('->')

def ndtv_news():
    news_list = []
    url = "https://www.ndtv.com/india#pfrom=home-ndtv_mainnavgation"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    lists = soup.find_all('div', class_="news_Itm-cont")

    for i, list in enumerate(lists):
        news_title = list.find('h2', class_="newsHdng").text.strip()
        date = list.find('span', class_="posted-by").text.strip()
        topic = list.find('p', class_="newsCont").text.strip()
        links = list.find('h2').a.get("href")

        news_list.append(links)
        news_list.append(news_title)
        news_list.append(date)
        news_list.append(topic)

        if l not in news_list:
            with open(f'news/{i}.csv', 'w') as f:
                f.write(f'{news_title}\n')
                f.write(f"{date}\n")
                f.write(f'{topic}\n')
            print(f'saved: {i}')
if __name__ == '__main__':
    while True:
        ndtv_news()
        wait = 10
        print(f"waiting {wait} minutes")
        time.sleep(wait * 60)





            # r = (f"{link}'\n' News_Headline --> {news_title}'\n' Posted By --> {date}'\n' News --> {topic}")
            # print(r)
    # print(news_list)




































