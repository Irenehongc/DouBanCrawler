from get_http_response import get


def get_commenter_uid(review_urls):
    uid = ''
    return uid


def get_reviews_by_movie_id(movie_id):
    url = "https://movie.douban.com/subject/%s/reviews" % movie_id
    response = get(url)
    #   获取所有影评的链接
    review_urls = response['']
    review_info = {'movie_id': movie_id}
    for url in review_urls:
        review_id = '解析url获得review_id'
        review = get_reviews_info(review_id)
        uid = get_commenter_uid(url)
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