import movie
import movie_all
from mysql import MyConnection
import time


url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=1000'

my_connection = MyConnection()
results = movie_all.get_is_download_movie(my_connection)
is_download = []
for item in results:
    is_download.append(item['movie_id'])
# print(is_download)
movies = movie_all.get_movie_all(url)
for movie_id in movies:
    if movie_id not in is_download:
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
