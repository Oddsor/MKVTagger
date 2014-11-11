import json
import requests

__author__ = 'Odd'


api_key = "f2fa46c4a4c90426317d7be92ac4474d"
poster_thumbnails = "https://image.tmdb.org/t/p/w185"

#tags = {'collection' 'movie' 'summary' 'companies' 'tagline' 'releasedate' 'actors': [['Chris Evans', 'Captain America'] 'director': ['Joe Russo', 'Anthony Russo']}


def search(movie_name):
    """movie_name (string) -> list(list(movie_name, image_thumbnail))"""
    request = requests.get(
        'http://api.themoviedb.org/3/search/movie?api_key=' + api_key + '&query=' + movie_name)
    searchjson = json.loads(request.text)
    movie_result = list()
    for result in searchjson['results']:
        movie_result.append([result['title'], result['release_date'][0:result['release_date'].index('-')], poster_thumbnails + result['poster_path'], result['id']])
    return movie_result

def get_info(id):
    request = requests.get(
        'http://api.themoviedb.org/3/movie/' + id + '?api_key=' + api_key + '&append_to_response=credits')
    searchjson = json.loads(request.text)
    movie_info = dict()
    if searchjson['belongs_to_collection'] is not None:
        movie_info['collection'] = searchjson['belongs_to_collection']['name']
    movie_info['movie'] = searchjson['original_title']
    movie_genres = list()
    for genre in searchjson['genres']:
        movie_genres.append(genre['name'])
    movie_info['genres'] = movie_genres
    movie_info['summary'] = searchjson['overview']
    movie_info['tagline'] = searchjson['tagline']
    movie_info['releasedate'] = searchjson['release_date']
    production_companies = list()
    for company in searchjson['production_companies']:
        production_companies.append(company['name'])
    if production_companies:
        movie_info['production_companies'] = production_companies
    cast = list()
    for actor in searchjson['credits']['cast']:
        cast.append([actor['name'], actor['character']])
    movie_info['actors'] = cast

    crew = dict()
    for crewjson in searchjson['credits']['crew']:
        if crewjson['job'] in crew:
            crew[crewjson['job']].append(crewjson['name'])
        else:
            crew[crewjson['job']] = [crewjson['name']]
    movie_info['crew'] = crew
    return {'item_info': movie_info}

if __name__ == '__main__':
    #print(search("Captain America"))
    #print(get_info('100402'))
    print(get_info('13995'))