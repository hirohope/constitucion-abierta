'''
input:
  'words': {'meaningful-word 1': {'L': 'lemma1', ...},
            'meaningful-word 2': {'L': 'lemma2', ...}, ...}

output:
  'lemmas': {'lemma 1': {'w': {word11, word12, ...}, ...},
             'lemma 2': {'w': {word21, word22, ...}, ...},
             ...}
'''
def add_lemwords(data):    
    lemmas = data['lemmas']
    for lemdata in lemmas.values():
        lemdata['w'] = set()
    
    words = data['words']
    for word in words:
        lemma = words[word]['L']
        lemmas[lemma]['w'].add(word)
