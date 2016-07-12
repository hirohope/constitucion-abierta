import nltk
from functions_txts import word_simplify
stemmer = nltk.stem.snowball.SnowballStemmer('spanish')

'''
input:
  'words': {'meaningful-word 1': {...}, 'meaningful-word 2': {...}, ...}
  'lemcorrections': {'representative1': {'word1', 'word2', ...}}

output:
  'words': {'meaningful-word 1': {'L': 'lemma1', ...},
            'meaningful-word 2': {'L': 'lemma2', ...}, ...}
'''
def add_lemmas(data):
    words = data['words']
    for re, lcwords in data['lemcorrections'].items():
        lemma = unique_lemma(re[1:]) if re[0]=='*' else noncorrected_lemma(re)
        for word in lcwords:
            words[word]['L'] = lemma
    
    for word, worddata in words.items():
        if 'L' not in worddata:
            worddata['L'] = noncorrected_lemma(word)

def unique_lemma(word):
    return word+'hh'

def noncorrected_lemma(word):
    return str(stemmer.stem(word_simplify(word)))
