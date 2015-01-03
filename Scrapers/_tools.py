__author__ = 'Odd'
import configparser
def get_apikey(keyname):
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return config['API_KEYS'][keyname]