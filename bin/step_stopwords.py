import nltk
from functions_txts import read_contents, word_simplify
from functions_cli import error_then_exit

'''
input:
  'stop-words.txt': 'file.txt'

output:
  'stop-words': {'stopword 1', 'stopword 2', ...}
'''
def add_stopwords(data):
    contents = read_contents(data['stop-words.txt'])
    stopwords = contents.splitlines()
    stopwords = map(word_simplify, stopwords)
    stopwords += nltk.corpus.stopwords.words('spanish')
    data['stop-words'] = set(stopwords)

'''
input:
  'no-stop-words.txt': 'file.txt'

output:
  'no-stop-words': {'no-stopword 1': discount1, 'no-stopword 2': discount2, ...}
'''
def add_nostopwords(data):
    data['no-stop-words'] = {}
    nostopwords = data['no-stop-words']
    contents = read_contents(data['no-stop-words.txt'])
    lines = contents.splitlines()
    for line in lines:
        line = line.split()
        if len(line) == 0: continue
        if len(line) == 1: line.append('1')
        if len(line) != 2: error_then_exit("bad line in no-stop-words")
        nostopword, discount = word_simplify(line[0]), int(line[1])
        nostopwords[nostopword] = discount
