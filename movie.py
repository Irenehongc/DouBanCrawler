import json

from get_http_response import get


def get_movie_info(movie_id):
    movie = {}
    url = 'https://movie.douban.com/j/subject_abstract?subject_id=%s' % movie_id
    # print(url)
    response = get(url)
    response = response.decode()
    info = json.loads(response)['subject']
    if info['subtype'] == 'Movie':
        movie = {'id': movie_id, 'title': info['title'], 'douban_rate': info['rate'], 'directors': info['directors'],
                 'actors': info['actors'], 'duration': info['duration'], 'region': info['region'],
                 'genres': info['types'], 'release_year': info['release_year']}
        # vote_count = get_vote_count(movie_id)
        # movie['vote_count'] = vote_count
        # 'vote_count' is a dynamic number  -> value?
    return movie


def get_str(movie_info):
    information = ''
    for i in range(len(movie_info)):
        if i == 0:
            information = movie_info[i]
        else:
            information = information + ',' + movie_info[i]
    return information


def get_vote_count(movie_id):
    pass


def get_insert_sql(movie_info):
    directors = ''
    actors = ''
    region = ''
    genres = ''
    if isinstance(movie_info['directors'], list):
        directors = get_str(movie_info['directors'])

    if isinstance(movie_info['actors'], list):
        actors = get_str(movie_info['actors'])

    if isinstance(movie_info['region'], list):
        region = get_str(movie_info['region'])

    if isinstance(movie_info['genres'], list):
        genres = get_str(movie_info['genres'])

    sql = '''INSERT INTO movies_info(movie_id, movie_title, douban_rating, director, actors, runtime, region,
                       genres, release_year) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")''' \
          % (movie_info['id'],
             movie_info['title'],
             movie_info['douban_rate'],
             directors,
             actors,
             movie_info['duration'],
             region,
             genres,
             movie_info['release_year'])
    return sql
