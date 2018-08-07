from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36', 'referer':"movie.douban.com"}
url = 'https://movie.douban.com/subject/27133303/reviews'
review_html = requests.get(url,  headers=headers)
Soup = BeautifulSoup(review_html.text, 'html.parser')
# 获取总条数
review_num = Soup.find_all('span', class_='count')
print(review_num)

# 获取当页review_id
# all_rid = Soup.find_all('div', class_='review-short')
# for rid in all_rid:
#     review_id = rid.get('data-rid')
#     print(review_id)
