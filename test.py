import re
import requests
import time
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36', 'referer':"movie.douban.com"}
url = 'https://movie.douban.com/review/9431840/'
review_html = requests.get(url, headers=headers)
soup = BeautifulSoup(review_html.text, 'html.parser')
review = {}
# 获取rating#
review_rate = soup.find_all('header', class_='main-hd')
rating = re.search(r'allstar([0-9]+) main-title-rating', str(review_rate))
if rating is not None:
    rate = rating.group(1)
    review['rating'] = int(int(rate)/10)
else:
    review['rating'] = 0
print(review)
