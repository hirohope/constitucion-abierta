import nltk
stemmer = nltk.stem.snowball.SnowballStemmer('spanish')

'''
input:
  'words': {'meaningful-word 1': {...}, 'meaningful-word 2': {...}, ...}

output:
  'words': {'meaningful-word 1': {'L': 'lemma1', ...},
            'meaningful-word 2': {'L': 'lemma2', ...}, ...}
'''
def add_lemmas(data):
    words = data['words']
    for word in words:
        words[word]['L'] = str(stemmer.stem(word))
