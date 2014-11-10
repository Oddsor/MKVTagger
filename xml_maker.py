
__author__ = 'Odd'

from xml.etree import ElementTree as ET

class Tag(object):
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

def get_xml(structure):
    root = ET.Element("Tags")
    if 'collection' in structure:
        tag = add_tag(root, Target.collection)
        add_simple(tag, Tag.title, structure['collection'])
    if 'season' in structure:
        print('not yet implemented')
    if 'movie' in structure:
        tag = add_tag(root, Target.movie)
        add_simple(tag, Tag.title, structure['movie'])
        if 'director' in structure:
            for director in structure['director']:
                add_simple(tag, Tag.director, director)
        if 'actors' in structure:
            for actor in structure['actors']:
                actortag = add_simple(tag, Tag.actor, actor[0])
                character = add_simple(actortag, Tag.character, actor[1])
        if 'summary' in structure:
            add_simple(tag, Tag.summary, structure['summary'])


    tree = ET.ElementTree(root)
    print(ET.dump(tree))


if __name__ == "__main__":
    structure = {'collection': 'Marvel movies',
                 'movie': 'Captain America: The Winter Soldier',
                 'summary': 'After the cataclysmic events in New York with The Aven....',
                 'companies': ['Sony', 'Marvel', 'Disney'],
                 'tagline': 'In heroes we trust',
                 'releasedate': '2014-04-04',
                 'actors': [['Chris Evans', 'Captain America'],
                            ['Sammy Jackson', 'Nick Fury']],
                 'director': ['Joe Russo', 'Anthony Russo']}
    get_xml(structure)