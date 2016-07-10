from collections import defaultdict

'''
input:
  'words': {'meaningful-word 1': {'L': 'lemma1', 'p': [pos11, pos12, ...], ...},
            'meaningful-word 2': {'L': 'lemma2', 'p': [pos21, pos22, ...], ...},
            ...}
output:
  'lemmas': {'lemma 1': {'p': [pos11, pos12, ...], ...},
             'lemma 2': {'p': [pos21, pos22, ...], ...},
             ...}
'''
def add_lempositions(data):
    data['lemmas'] = defaultdict(lambda: {'p': []})
    lemmas = data['lemmas']
    words = data['words']
    for word in words:
        lemma = words[word]['L']
        wordpositions = words[word]['p']
        lemmas[lemma]['p'] += wordpositions
