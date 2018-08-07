import requests
import time
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36', 'referer':"movie.douban.com"}
url = 'https://movie.douban.com/subject/27133303/reviews'
review_html = requests.get(url,  headers=headers)
Soup = BeautifulSoup(review_html.text, 'html.parser')
# 获取总条数
review_num = Soup.find_all('span', class_='count')
review_num = str(review_num).replace('[<span class="count">(共', '').replace('条)</span>]', '')
print(review_num)


# 获取每一页的id
review_ids = []
for i in range(int(int(review_num)/20)):
    url = 'https://movie.douban.com/subject/27133303/reviews?sort=hotest&start=%d' % i*20
    review_html = requests.get(url, headers=headers)
    soup = BeautifulSoup(review_html.text, 'html.parser')

    # 再加一个判断：是否是折叠页

    all_rid = soup.find_all('div', class_='review-short')
    for rid in all_rid:
        review_id = rid.get('data-rid')
        review_ids.append(review_id)
    time.sleep(5)
print(review_ids)
