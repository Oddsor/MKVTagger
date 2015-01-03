import configparser
import json
import requests
from MKVTag import tagtools
from scrapers import _tools

__author__ = 'Odd'


poster_thumbnails_path = "http://image.tmdb.org/t/p/w185"
poster_path = 'http://image.tmdb.org/t/p/original'
backdrop_small_path = 'http://image.tmdb.org/t/p/w780'
backdrop_path = 'http://image.tmdb.org/t/p/original/'


#TODO make a translation tool (mkvtag = moviedbtag), difflib isn't as cool as expected
api_key = _tools.get_apikey('themoviedb')

def search(movie_name):
    """movie_name (string) -> list(list(movie_name, image_thumbnail))"""
    request = requests.get(
        'http://api.themoviedb.org/3/search/movie?api_key=' + api_key + '&query=' + movie_name)
    searchjson = json.loads(request.text)
    movie_result = list()
    for result in searchjson['results']:
        movie_result.append([result['title'], result['release_date'][0:result['release_date'].index('-')],
                             poster_thumbnails_path + result['poster_path'], result['id']])
    return movie_result

def get_info(id):
    request = requests.get(
        'http://api.themoviedb.org/3/movie/' + id + '?api_key=' + api_key + '&append_to_response=credits')
    searchjson = json.loads(request.text)
    collection_info = dict()
    if searchjson['belongs_to_collection'] is not None:
        for tag in searchjson['belongs_to_collection']:
            try:
                collection_info[tagtools.find_tagname(tag)] = searchjson['belongs_to_collection'][tag]
            except Exception:
                pass
    del searchjson['belongs_to_collection']
    genres = list()
    for genre in searchjson['genres']:
        genres.append(genre['name'])
    searchjson['genres'] = genres
    production_comp = list()
    for company in searchjson['production_companies']:
        production_comp.append(company['name'])
    del searchjson['production_companies']
    del searchjson['production_countries']
    searchjson['production_studio'] = production_comp
    item_info = dict()
    for crewmember in searchjson['credits']['crew']:
        if crewmember['job'] in ['Set Decoration', 'Sculptor']:
            pass
        elif crewmember['job'] in searchjson:
            searchjson[crewmember['job']].append(crewmember['name'])
        else:
            searchjson[crewmember['job']] = [crewmember['name']]
    actors = list()
    for actor in searchjson['credits']['cast']:
        actors.append([actor['name'], actor['character']])
    searchjson['actor'] = actors
    del searchjson['credits']
    for tag in searchjson:
        try:
            item_info[tagtools.find_tagname(tag)] = searchjson[tag]
        except Exception:
            pass
    appendages = dict()
    appendages['cover_small.jpg'] = poster_thumbnails_path + searchjson['poster_path']
    appendages['cover_land.jpg'] = backdrop_path + searchjson['backdrop_path']
    appendages['cover.jpg'] = poster_path + searchjson['poster_path']
    appendages['cover_land_small.jpg'] = backdrop_small_path + searchjson['backdrop_path']
    return {'collection': collection_info, 'item': item_info, 'attachments': appendages}

if __name__ == '__main__':
    #print(search("Captain America"))
    print(get_info('100402'))
    #print(get_info('13995'))