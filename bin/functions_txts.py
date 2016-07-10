import codecs, unicodedata

def read_contents(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        return f.read()

def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    try:
        return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')
    except Exception, e:
        raise e

def word_simplify(word):
    if type(word) is str: word = unicode(word, 'utf-8')
    return str(remove_diacritic(word).lower())
