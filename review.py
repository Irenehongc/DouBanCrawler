import re
import requests
import time
from get_http_response import get
from bs4 import BeautifulSoup


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

    review_info = []
    for review_id in review_ids:
        # review = {review_content:text, rating:star, helpfulness:vote, useless:vote, commenter_id:uid, review_id:id, forwarding_num:num}
        review = get_reviews_info(review_id)
        review_info.append(review)
    return review_info
    

def get_reviews_info(review_id):
    #   解析评论内容、用户打分、转发数、有用数、无用数、commenter_id
    review = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'referer': "movie.douban.com"}
    url = 'https://movie.douban.com/review/%s/' % review_id
    review_html = requests.get(url, headers=headers)
    soup = BeautifulSoup(review_html.text, 'html.parser')
    review = {}
    # 获取rating
    review_rate = soup.find_all('header', class_='main-hd')
    rating = re.search(r'allstar([0-9]+) main-title-rating', str(review_rate))
    if rating is not None:
        rate = rating.group(1)
        review['rating'] = int(int(rate) / 10)
    else:
        review['rating'] = 0

    # 有用数、无用数
    useful_class = "btn useful_count %s j a_show_login" % review_id
    useful_count = soup.find_all('button', class_=useful_class)
    useful_count = useful_count.replace('<button class="btn useful_count 9371524 j a_show_login"> 有用 ', '').replace('</button>', '')
    
    useless_class = "btn useless_count %s j a_show_login" % review_id
    useless_count = soup.find_all('button', class_=useless_class)
    useless_count = useless_count.replace('<button class="btn useless_count 9371524 j a_show_login"> 无用 ', '').replace('</button>', '')

    # 转发数
    # <span class="rec-num">9</span>
    rec_num = soup.find_all('span', class_='rec-num')
    if rec_num is not None:
        review['forwarding_num'] = rec_num
    else:
        review['forwarding_num'] = 0
    
    # 评论者id
    # <a class="avatar author-avatar left" href="https://www.douban.com/people/3540441/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u3540441-63.jpg"></a>
    commenter_url = soup.find('a', class_='avatar author-avatar left').get('href')
    commenter_id = commenter_url.split('/')[-2]
    review['commenter_id'] = commenter_id

    # 内容
    # <div property="v:description" class="review-content clearfix" data-author="同志亦凡人中文站" data-url="https://movie.douban.com/review/9245707/" data-original="1">
    content_tag = soup.find('div', class_='review-content clearfix')
    content = content_tag.get('p')
    review['review_content'] = content
    return review


def write_to_mysql(review_info, movie_id):
    # 批量录入mysql
    sql = '''insert into review (review_id, movie_id, commenter_id, rating, useful_count, useless_count, forwarding_num, review_content) 
            values()'''
            