__author__ = 'Odd'
import configparser
import requests
import json

config = configparser.ConfigParser()
#name = input("Enter api name:")
name = "themoviedssb"
if len(config.read(name + ".ini")) != 0:
    print(name + ".ini already exists")
    exit(404)
config.set('DEFAULT', 'api_key', "f2fa46c4a4c90426317d7be92ac4474d")
#config.set('DEFAULT', 'api_key', input("API key:"))
config.add_section('URLS')
#config.set('URLS', 'search', input("Search url:"))
config.set('URLS', 'search', "http://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}")
#config.set('URLS', 'data', input("Data url:"))
config.set('URLS', 'data', "http://api.themoviedb.org/3/movie/{id}?api_key={api_key}&append_to_response=credits")

settings = configparser.ConfigParser()
settings.read('settings.ini')
apikey = config['DEFAULT']['api_key']
search_test = requests.get(config['URLS']['search'].format(api_key=apikey, query=input("Search-test - show name:")))
print(str(search_test.text))
request = requests.get(config['URLS']['data'].format(api_key=apikey, id=input("Data test - show id:")))
#jsonres = json.load(request.text)
print(str(request.text))

#config.write(name + ".ini")