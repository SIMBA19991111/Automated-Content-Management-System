#媒体评价页标签 /  Media Views Label

critic_values = []
review_grades = []
review_bodys = []
temp_critic_values = []
game_names = []
n = 0
x = 0
import bs4 as BeautifulSoup
import requests
import pandas as pd
import fake_useragent
from fake_useragent import UserAgent

# requests带上自己浏览器信息的请求头，默认允许重定向
headers = {"user-agent": UserAgent().random}
urls = []
i = 0
while i < 15:
    page = requests.get(
        'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2022&distribution=&sort=desc&view=detailed&page=' + str(
            i), headers=headers)
    i = i + 1

    soup = BeautifulSoup.BeautifulSoup(page.content, 'html.parser')

    game_containers = soup.find_all('td', class_='clamp-summary-wrap')

    print("========================================")

    for container in game_containers:
        url = container.find('a', attrs={'class': 'title'})['href']
        urls.append('www.metacritic.com' + str(url))

url_folder = pd.DataFrame({'url': urls})
url_folder.to_csv('urls_2022.csv')

for each_url in urls:
    print(each_url)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
    }
    page1 = requests.get('http://' + str(each_url) + '/critic-reviews', headers=header)
    page2 = requests.get('http://' + str(each_url), headers=header)
    soup = BeautifulSoup.BeautifulSoup(page1.content, 'html.parser')
    soup2 = BeautifulSoup.BeautifulSoup(page2.content, 'html.parser')
    critic_containers_first = soup.find('li', class_='review critic_review first_review')
    critic_containers_last = soup.find('li', class_='review critic_review last_review')
    critic_containers = soup.find_all('li', class_='review critic_review')
    detail_containers = soup2.find('div', class_='left')
    game_title = detail_containers.select('h1', class_='product_title')[0].get_text()
    print(game_title)

    # 第一个评论的媒体名称

    critic_value_first = critic_containers_first.select('.review_critic div')[0].get_text()
    critic_values.append(str.strip(critic_value_first))

    # 第一个评论的媒体得分
    review_grade_first = critic_containers_first.select('.review_grade div')[0].get_text()
    review_grades.append(review_grade_first)

    # 第一个评论的媒体内容
    review_body_first = critic_containers_first.select('div', class_='review_section')[12].get_text()
    review_bodys.append(str.strip(review_body_first))

    for container in critic_containers:
        critic_value = container.select('.review_critic div')[0].get_text()
        critic_values.append(critic_value)
        review_grade = container.select('.review_grade div')[0].get_text()
        review_grades.append(review_grade)
        #        if  review_grade:
        #            review_grades.append(review_grade)
        #        else:
        #            continue
        review_body = container.select('div', class_='review_section')[12].get_text()
        review_bodys.append(str.strip(review_body))

    # 最后一个评论的媒体名称
    critic_value_last = critic_containers_last.select('.review_critic div')[0].get_text()
    critic_values.append(critic_value_last)

    # 最后一个评论的媒体得分
    review_grade_last = critic_containers_last.select('.review_grade div')[0].get_text()
    review_grades.append(review_grade_last)

    # 最后一个评论的媒体内容
    review_body_last = critic_containers_last.select('div', class_='review_section')[12].get_text()
    review_bodys.append(str.strip(review_body_last))
    print(len(critic_values)+2)

    # 使game_title的数组长度和其他的一样
    while n <= (len(critic_values) - len(temp_critic_values)):
        n = n + 1
        game_names.append(game_title)
    temp_critic_values.append(critic_values)
    # 测试用，缩短爬虫时间，最后删

print(len(critic_values))
print(len(review_grades))
print(len(review_bodys))
print(len(game_names))

every_critic_folder = pd.DataFrame({'game_names': game_names,
                                    'critic_values': critic_values,
                                    'review_grades': review_grades,
                                    'review_bodys': review_bodys})
print(every_critic_folder)
every_critic_folder.to_csv('test4.csv')

