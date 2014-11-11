
__author__ = 'Odd'

from xml.etree import ElementTree as ET

class MkvTag(object):
    title = 'TITLE'
    director = 'DIRECTOR'
    actor = 'ACTOR'
    character = 'CHARACTER'
    summary = 'SUMMARY'

class Target(object):
    collection = '70'
    season = '60'
    movie = '50'
    episode = '50'

def add_tag(root, targetnumber):
    tag = ET.SubElement(root, "Tag")
    target = ET.SubElement(tag, "Target")
    target_type = ET.SubElement(target, "TargetTypeValue")
    target_type.text = targetnumber
    return tag

def add_simple(element, tagname, string):
    simple = ET.SubElement(element, 'Simple')
    name = ET.SubElement(simple, 'Name')
    name.text = tagname
    stringtag = ET.SubElement(simple, 'String')
    stringtag.text = string
    return simple

def get_xml(mediainfo):
    root = ET.Element("Tags")
    if 'collection' in mediainfo:
        tag = add_tag(root, Target.collection)
        add_simple(tag, MkvTag.title, mediainfo['collection'])
    if 'season' in mediainfo:
        print('not yet implemented')
    if 'movie' in mediainfo:
        tag = add_tag(root, Target.movie)
        add_simple(tag, MkvTag.title, mediainfo['movie'])
        if 'director' in mediainfo:
            for director in mediainfo['director']:
                add_simple(tag, MkvTag.director, director)
        if 'actors' in mediainfo:
            for actor in mediainfo['actors']:
                actortag = add_simple(tag, MkvTag.actor, actor[0])
                character = add_simple(actortag, MkvTag.character, actor[1])
        if 'summary' in mediainfo:
            add_simple(tag, MkvTag.summary, mediainfo['summary'])

    tree = ET.ElementTree(root)
    return ET.dump(tree)

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

if __name__ == "__main__":

    mediainfos = {'collection': 'Marvel movies',
                 'movie': 'Captain America: The Winter Soldier',
                 'summary': 'After the cataclysmic events in New York with The Aven....',
                 'companies': ['Sony', 'Marvel', 'Disney'],
                 'tagline': 'In heroes we trust',
                 'releasedate': '2014-04-04',
                 'actors': [['Chris Evans', 'Captain America'],
                            ['Sammy Jackson', 'Nick Fury']],
                 'director': ['Joe Russo', 'Anthony Russo']}
    get_xml(mediainfos)