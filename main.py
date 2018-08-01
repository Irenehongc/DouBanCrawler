#
#   影片详细信息url https://movie.douban.com/j/subject_abstract?subject_id=27113517
#   加载更多url https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&
#                       page_limit=20&page_start=20
#   标签电影url https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=1000
#

from movie_all import get_movie_all
import movie
from mysql import MyConnection
import time


#   热门标签电影
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=1000'


my_connection = MyConnection()
movies = get_movie_all(url)
# print(movies)
for movie_id in movies:
    movie_info = movie.get_movie_info(movie_id)
    sql = movie.get_insert_sql(movie_info)
    # print(sql)
    # input("x: ")
    try:
        my_connection.execute(sql)
    except BaseException:
        print(sql)
    time.sleep(10)

my_connection.close()
