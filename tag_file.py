__author__ = 'Odd'

import argparse

# parser = argparse.ArgumentParser(description="Tag file with data from link")
# parser.add_argument('API_SOURCE', help="The rest api with json or xml data")
# parser.add_argument('FILE', help="The file getting tagged")
# parser.add_argument('-t', help="Thorough-mode, enables file length check", action='store_true')
# parser.add_argument('-a', help="Anime shows", action='store_true')

url = 'http://api.themoviedb.org/3/movie/{id}?api_key={api_key}&append_to_response=credits'.format(id=22, api_key="test")
print(url)