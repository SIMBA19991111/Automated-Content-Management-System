from bs4 import BeautifulSoup
import requests
import pandas as pd

#Take year 2022 as an example
headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (Windows NT 10.0;"}
urls =[]
i = 0
while i < 15:
    page=requests.get('https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2022&distribution=&sort=desc&view=detailed&page='+str(i),headers=headers)
    i = i+1
    print(page.content)

    soup = BeautifulSoup(page.content, 'html.parser')

    game_containers = soup.find_all('td', class_ = 'clamp-summary-wrap')
    print(type(game_containers))

    print("========================================")

    for container in game_containers:
        url = container.find('a', attrs={'class': 'title'})['href']
        urls.append('www.metacritic.com'+str(url))

    print(urls)

url_folder = pd.DataFrame({'url': urls})
url_folder.to_csv('urls_2022_.csv')
