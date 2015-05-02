from xml.etree import ElementTree as ET

import requests
from MKVTag.scrapers import _tools


__author__ = 'Odd'

cover_path = "http://thetvdb.com/banners/"

collection_cache = dict()


def search(tv_show):
    request = requests.get('http://thetvdb.com/api/GetSeries.php?seriesname=' + tv_show)
    root = ET.fromstring(request.text)
    results = list()
    for series in root.findall('Series'):
        print(series.find('banner'))
        results.append({'title': series.find('SeriesName').text, 'thumbnail': "" if series.find('banner') is None else
                cover_path + series.find('banner').text, 'id': series.find('id').text,
                'release': "" if series.find('FirstAired') is None else
                series.find('FirstAired').text[0:series.find('FirstAired').text.index('-')]})
    return results


def get_info(title_id, season=None, episode=None):
    appendages = dict()
    if title_id not in collection_cache:
        request = requests.get("http://thetvdb.com/api/" + _tools.get_apikey("thetvdb") + "/series/" + str(title_id) + "/")
        collection_cache[title_id] = request.text
        root = ET.fromstring(request.text)
    else:
        root = ET.fromstring(collection_cache[title_id])
    series = root.findall('Series')[0]
    collection_info = dict()
    genres = list()
    for item in str(series.find('Genre').text).split('|'):
        if len(item) != 0:
            genres.append(item)
    collection_info['GENRE'] = genres
    collection_info['TITLE'] = series.find('SeriesName').text
    collection_info['SUMMARY'] = series.find('Overview').text
    appendages['cover_land.jpg'] = cover_path + series.find('fanart').text
    appendages['cover.jpg'] = cover_path + series.find('poster').text

    season_info = dict()
    item_info = dict()

    if season is not None and episode is not None:
        request = requests.get("http://thetvdb.com/api/" + _tools.get_apikey("thetvdb") + "/series/" + str(title_id)
                               + "/default/" + str(season) + "/" + str(episode) + "/en.xml")
        root = ET.fromstring(request.text)
        episode = root.findall('Episode')[0]
        item_info['TITLE'] = episode.find('EpisodeName').text
        item_info['PART_NUMBER'] = episode.find('EpisodeNumber').text
        season_info['PART_NUMBER'] = episode.find('SeasonNumber').text
        item_info['SUMMARY'] = episode.find('Overview').text

    # production_comp = list()
    # for company in searchjson['production_companies']:
    #     production_comp.append(company['name'])
    # del searchjson['production_companies']
    # del searchjson['production_countries']
    # searchjson['production_studio'] = production_comp
    # item_info = dict()
    # for crewmember in searchjson['credits']['crew']:
    #     if crewmember['job'] in ['Set Decoration', 'Sculptor']:
    #         pass
    #     elif crewmember['job'] in searchjson:
    #         searchjson[crewmember['job']].append(crewmember['name'])
    #     else:
    #         searchjson[crewmember['job']] = [crewmember['name']]
    # actors = list()
    # for actor in searchjson['credits']['cast']:
    #     actors.append([actor['name'], actor['character']])
    # searchjson['actor'] = actors
    # del searchjson['credits']
    # for tag in searchjson:
    #     try:
    #         item_info[tagtools.find_tagname(tag)] = searchjson[tag]
    #     except Exception:
    #         pass

    return {'collection': collection_info, 'season': season_info, 'item': item_info, 'attachments': appendages}


if __name__ == '__main__':
    #print(search("Attack on Titan"))
    print(get_info('251085', 1, 10))
    #print(get_info('13995'))