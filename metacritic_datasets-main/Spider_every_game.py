#游戏详情页标签 /  Game Details Label
#以2022年为例，通过前一层网页爬取所有2022年各游戏的URL，遍历访问每个游戏URL进一步爬取相关数据
#Taking 2022 as an example, get the URLs of all games in 2022 through the previous layer of web pages, and traverse through each game URL to obtain relevant data
from bs4 import BeautifulSoup
import requests
import pandas as pd
headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (Windows NT 10.0;"}

game_titles = []
game_platforms = []
game_publishers = []
game_dates = []
critic_rating_values = []
user_rating_values = []
user_rating_nos = []
user_rating_developers = []
game_levels = []
game_genres = []
urls = []
i = 0


while i < 15:
    page = requests.get('https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2022&distribution=&sort=desc&view=detailed&page=' + str(i), headers=headers)
    i = i + 1

    soup = BeautifulSoup(page.content, 'html.parser')

    game_containers = soup.find_all('td', class_='clamp-summary-wrap')

    print("========================================")

    for container in game_containers:
        url = container.find('a', attrs={'class': 'title'})['href']
        urls.append('www.metacritic.com' + str(url))

url_folder = pd.DataFrame({'url': urls})
url_folder.to_csv('urls_game_2022.csv')

for url in urls:
   
    headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (Windows NT 10.0;"}
    page1=requests.get('https://'+str(url),headers=headers)
    soup = BeautifulSoup(page1.content, 'html.parser')
    detail_containers = soup.find('div', class_ = 'left')

    '''game_title游戏名称'''
    game_title = detail_containers.select('h1',class_ = 'product_title')[0].get_text()
    print(game_title)
    game_titles.append(game_title)

    '''game_platform游戏平台'''
    game_platform = detail_containers.select('.platform a')[0].get_text()
    print(str.strip(game_platform))
    game_platforms.append(game_platform)

    '''game_publisher游戏发行商'''
    game_publisher = detail_containers.select('span',class_ = 'summary_details')[6].get_text()
    print(str.strip(game_publisher))
    game_publishers.append(game_publisher)

    '''game_date游戏发行日期'''
    game_date = detail_containers.select('span',class_ = 'summary_details')[8].get_text()
    print(str.strip(game_date))
    game_dates.append(game_date)

    '''critic_value媒体综评'''
    critic_rating_value = detail_containers.select('.summary_wrap div')[5].get_text()
    print(str.strip(critic_rating_value))
    critic_rating_values.append(critic_rating_value)

    '''user_rating_value用户评分'''
    user_rating_value = detail_containers.select('.summary_wrap div')[11].get_text()
    print(str.strip(user_rating_value))
    user_rating_values.append(user_rating_value)

    '''user_rating_no用户评论数'''
    user_rating_no = detail_containers.select('.count a')[1].get_text()
    print(str.strip(user_rating_no))
    user_rating_nos.append(user_rating_no)

    '''user_developer游戏开发者'''
    user_rating_developer = detail_containers.select('.data a')[2].get_text()
    print(str.strip(user_rating_developer))
    user_rating_developers.append(user_rating_developer)

    '''game_genre游戏流派'''
    genre_containers = detail_containers.find('li', class_ = 'summary_detail product_genre')
    print(genre_containers)
    game_genre = genre_containers.select('span', class_ = 'data' )
    print(game_genre)
    game_genres.append(game_genre)

    '''game_level游戏评级'''
    game_level = detail_containers.select('.summary_details  span')[22].get_text()
    print(str.strip(game_level))
    game_levels.append(game_level)

print(len(game_titles))
print(len(game_platforms))
print(len(game_publishers))
print(len(game_dates))
print(len(critic_rating_values))
print(len(user_rating_values))
print(len(user_rating_nos))
print(len(user_rating_developers))
print(len(game_levels))
print(len(game_genres))

every_critic_folder = pd.DataFrame({'game_titles': game_titles,
                                   'game_platforms': game_platforms,
                                    'game_publishers': game_publishers,
                                    'game_dates': game_dates,
                                    'critic_rating_values': critic_rating_values,
                                    'user_rating_values': user_rating_values,
                                    'user_rating_nos': user_rating_nos,
                                    'user_rating_developers': user_rating_developers,
                                    'game_levels': game_levels,
                                    'game_genres': game_genres})
print(every_critic_folder)
every_critic_folder.to_csv('testfinal.csv')
