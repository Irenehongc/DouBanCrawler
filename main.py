#
#   影片详细信息url https://movie.douban.com/j/subject_abstract?subject_id=27113517
#   加载更多url https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&
#                       page_limit=20&page_start=20
#   标签电影url https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=1000
#

import movie_all
import review
from mysql import MyConnection
import time


#   热门标签电影
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=1000'


my_connection = MyConnection()
# 获取已下载的电影id
results = movie_all.get_is_download_movie(my_connection)
is_download = []
for item in results:
    is_download.append(item['movie_id'])

for item in is_download:
    # 遍历每部电影的影评
    reviews_info = review.get_reviews_by_movie_id(item)

my_connection.close()
