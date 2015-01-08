from OddTools import oddconfig

__author__ = 'Odd'


def get_apikey(keyname):
    oddconfig.read('../settings.ini')
    return oddconfig.get_setting(keyname, 'API_KEYS')
