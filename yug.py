from bs4 import BeautifulSoup
import requests

url = 'https://www.ndtv.com/india#pfrom=home-ndtv_mainnavgation'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="news_Itm")

for list in lists:
    title = list.find('h2', class_="newsHdng")
    date = list.find('span', class_="posted-by")
    content = list.find('p', class_="newsCont")
    info = [title, date, content]
    print(info)