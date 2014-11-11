import json
import requests

__author__ = 'Odd'

api_key = "f2fa46c4a4c90426317d7be92ac4474d"
poster_thumbnails = "https://image.tmdb.org/t/p/w185"

def search(tv_show):
    """movie_name (string) -> list(list(tv_show, image_thumbnail))"""
    request = requests.get(
        'http://api.themoviedb.org/3/search/tv?api_key=' + api_key + '&query=' + tv_show)
    searchjson = json.loads(request.text)
    tv_result = list()
    for result in searchjson['results']:
        tv_result.append([result['name'], result['first_air_date'][0:result['first_air_date'].index('-')], poster_thumbnails + result['poster_path'], result['id']])
    return tv_result

def get_info(id):
    request = requests.get(
        'http://api.themoviedb.org/3/tv/' + id + '?api_key=' + api_key + '&append_to_response=credits')
    searchjson = json.loads(request.text)

if __name__ == '__main__':
    print(search("Attack on Titan"))
    #print(get_info('100402'))
    #print(get_info('13995'))