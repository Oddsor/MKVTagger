from OddTools import oddconfig
import os

__author__ = 'Odd'


def get_apikey(keyname):
    oddconfig.read(os.path.dirname(__file__).rsplit('\\', maxsplit=1)[0].rsplit('\\', maxsplit=1)[0] + '\settings.ini')
    return oddconfig.get_setting(keyname, 'API_KEYS')
