import json
from get_http_response import get


def get_movie_all(url):
    movies_id = []
    response = get(url)
    response = response.decode()
    # print(type(response))
    # print(response)
    movies_info = json.loads(str(response))
    # print(type(movies_info))
    movies = movies_info['subjects']
    for item in movies:
        movie_id = item['id']
        movies_id.append(movie_id)
    # print(movies_id)
    return movies_id


def get_is_download_movie(connection):
    sql = 'select movie_id from movies_info group by movie_id'
    results = connection.get_result(sql)
    return results
