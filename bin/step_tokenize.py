import nltk, re, string, unicodedata
from functions_txts import read_contents, word_simplify
sim = word_simplify
#table = string.maketrans("", "")

'''
input:
  txt = 'file.txt'
  stopwords = {'stopword 1', 'stopword 2', ...}

output:
  tokens = ['meaningful-word 1', 'meaningful-word 2', ...]
'''
def meaningfulword_tokenize(txt, stopwords):    
    contents = read_contents(txt)
    tokens = nltk.word_tokenize(contents)
    #tokens = map(word_simplify, tokens)
    tokens = [t.lower() for t in tokens]
    #tokens = [t.translate(table, string.punctuation) for t in tokens]
    #tokens = [t.translate(dict.fromkeys(string.punctuation)) for t in tokens]
    tokens = map(word_clean, tokens)
    tokens = filter(is_word, tokens)
    #tokens = [t for t in tokens if re.match('[a-zA-Z]', sim(t))]
    tokens = [t for t in tokens if sim(t) not in stopwords and len(t) > 2]
    #tokens = map(lambda t: t + 's' if t=='derecho' else t, tokens)
    return tokens

acceptable = set(('Lu', 'Ll', 'Lm'))
def word_clean(word):
    return u''.join([c for c in word if unicodedata.category(c) in acceptable])

def is_word(word):
    return True
