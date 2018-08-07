import requests
import time

from get_http_response import get
from bs4 import BeautifulSoup


def get_commenter_uid(review_urls):
    uid = ''
    return uid


def get_reviews_url(movie_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'referer': "movie.douban.com"}
    url = 'https://movie.douban.com/subject/%s/reviews' % movie_id
    review_html = requests.get(url, headers=headers)
    Soup = BeautifulSoup(review_html.text, 'html.parser')
    # 获取总条数
    review_num = Soup.find_all('span', class_='count')
    review_num = str(review_num).replace('[<span class="count">(共', '').replace('条)</span>]', '')
    # print(review_num)

    # 获取每一页的id
    review_ids = []
    for i in range(int(int(review_num) / 20)):
        url = 'https://movie.douban.com/subject/%s/reviews?sort=hotest&start=%d' % movie_id, i * 20
        review_html = requests.get(url, headers=headers)
        soup = BeautifulSoup(review_html.text, 'html.parser')

        # 再加一个判断：是否是折叠页

        all_rid = soup.find_all('div', class_='review-short')
        for rid in all_rid:
            review_id = rid.get('data-rid')
            review_ids.append(review_id)
        time.sleep(5)
    print(review_ids)
    return review_ids


def get_reviews_by_movie_id(movie_id):
    #   获取所有影评的链接id
    review_ids = get_reviews_url(movie_id)

    review_info = {'movie_id': movie_id}
    for review_id in review_ids:
        review = get_reviews_info(review_id)
        uid = get_commenter_uid(review_id)
        review_info['review_id'] = review_id
        review_info['uid'] = uid
        review_info['content'] = review['content']
        pass
    return review_info
    

def get_reviews_info(review_id):
    url = 'https://movie.douban.com/review/%s/' % review_id
    response = get(url)
    #   解析评论内容、用户打分、转发数、有用数、无用数、是否是最佳评论
    return response


def write_to_mysql(review):
    sql = "insert into review values()"