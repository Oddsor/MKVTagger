import difflib

__author__ = 'Odd'

taglist = ['TOTAL_PARTS', 'PART_NUMBER', 'PART_OFFSET', 'TITLE', 'SUBTITLE', 'ARTIST', 'LEAD_PERFORMER',
           'ACCOMPANIMENT', 'COMPOSER', 'ARRANGER', 'LYRICS', 'LYRICIST', 'CONDUCTOR',
           'DIRECTOR', 'ASSISTANT_DIRECTOR', 'DIRECTOR_OF_PHOTOGRAPHY', 'SOUND_ENGINEER', 'ART_DIRECTOR',
           'PRODUCTION_DESIGNER', 'CHOREOGRAPHER', 'COSTUME_DESIGNER', 'ACTOR', 'CHARACTER', 'WRITTEN_BY',
           'SCREENPLAY_BY', 'EDITED_BY', 'PRODUCER', 'COPRODUCER', 'EXECUTIVE_PRODUCER', 'DISTRIBUTED_BY',
           'MASTERED_BY', 'ENCODED_BY', 'MIXED_BY', 'PRODUCTION_STUDIO', 'THANKS_TO', 'PUBLISHER', 'LABEL', 'GENRE',
           'MOOD', 'ORIGINAL_MEDIA_TYPE', 'CONTENT_TYPE', 'SUBJECT', 'DESCRIPTION', 'KEYWORDS', 'SUMMARY',
           'SYNOPSIS', 'INITIAL_KEY', 'PERIOD', 'LAW_RATING', 'ICRA', 'DATE_RELEASED', 'DATE_RECORDED', 'DATE_ENCODED',
           'DATE_TAGGED', 'DATE_DIGITIZED', 'DATE_WRITTEN', 'DATE_PURCHASED', 'RECORDING_LOCATION',
           'COMPOSITION_LOCATION', 'COMPOSER_NATIONALITY']

synonyms = {'TITLE': ['NAME', 'ORIGINAL_TITLE'],
            'SUBTITLE': ['TAGLINE'],
            'COMPOSER': 'ORIGINAL MUSIC COMPOSER'}

def find_tagname(word):
    """string -> string
    Tries to find the official tag name used in Matroska-files by checking which tag most closely resembles the word.

    For instance a tag called 'Producer' will be closer to the official tag 'PRODUCED_BY' than 'EXECUTIVE_PRODUCER'"""
    for newword in synonyms:
            if word.upper() in synonyms[newword]:
                return newword
    results = difflib.get_close_matches(word.upper(), taglist)
    if not results:
        raise Exception("Word not found: " + word)
    else:
        return results[0]

if __name__ == '__main__':
    print(find_tagname(''))
    #print(get_info('100402'))
    #print(get_info('13995'))