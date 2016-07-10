import nltk, re, string
from functions_txts import read_contents, word_simplify
table = string.maketrans("", "")

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
    tokens = map(word_simplify, tokens)
    tokens = [t.translate(table, string.punctuation) for t in tokens]
    tokens = [t for t in tokens if re.match('[a-zA-Z]', t)]
    tokens = [t for t in tokens if t not in stopwords and len(t) > 2]
    tokens = map(lambda t: t + 's' if t=='derecho' else t, tokens)
    return tokens

