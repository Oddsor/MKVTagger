import requests
from xml.etree import ElementTree as ET

__author__ = 'Odd'

cover_path = "http://thetvdb.com/banners/"

def search(tv_show):
    request = requests.get('http://thetvdb.com/api/GetSeries.php?seriesname=' + tv_show)
    root = ET.fromstring(request.text)
    results = list()
    for series in root.findall('Series'):
        results.append([series.find('SeriesName').text, cover_path + series.find('banner').text, series.find('id').text])
    return results

def get_info(id):
    pass

if __name__ == '__main__':
    print(search("Attack on Titan"))
    #print(get_info('267440'))
    #print(get_info('13995'))