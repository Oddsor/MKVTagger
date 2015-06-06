__author__ = 'Odd'

import argparse
import configparser

# parser = argparse.ArgumentParser(description="Tag file with data from link")
# parser.add_argument('API_SOURCE', help="The rest api with json or xml data")
# parser.add_argument('FILE', help="The file getting tagged")
# parser.add_argument('-t', help="Thorough-mode, enables file length check", action='store_true')
# parser.add_argument('-a', help="Anime shows", action='store_true')

config = configparser.ConfigParser()
config.read('settings.ini')
print(str(config['XML_TAGS']['tags'].split('\n')))