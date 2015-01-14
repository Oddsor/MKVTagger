
__author__ = 'Odd'

from xml.etree import ElementTree as ET
from Scrapers import themoviedb

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
        for item in mediainfo['collection']:
            add_simple(tag, item, mediainfo['collection'][item])
    if 'season' in mediainfo:
        print('not yet implemented')
    if 'item' in mediainfo:
        tag = add_tag(root, Target.movie)
        for itemtag in mediainfo['item']:
            if itemtag == 'ACTOR':
                for actor in mediainfo['item'][itemtag]:
                    act = add_simple(tag, itemtag, actor[0])
                    add_simple(act, 'CHARACTER', actor[1])
            elif isinstance(mediainfo['item'][itemtag], list):
                for item in mediainfo['item'][itemtag]:
                    add_simple(tag, itemtag, item)
            else:
                add_simple(tag, itemtag, mediainfo['item'][itemtag])

    return ET.tostring(root, encoding="unicode")

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

    print(get_xml(themoviedb.get_info('100402')))