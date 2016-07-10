from retruchery import choose_representative

'''
input:
  'lemmas': {'lemma 1': {'w': {word11, word12, ...}, ...},
             'lemma 2': {'w': {word21, word22, ...}, ...},
             ...}

output:
  'lemmas': {'lemma 1': {'r': 'representative1', ...},
             'lemma 2': {'r': 'representative2', ...},
             ...}
'''
def add_lemrepresentatives(data):
    for lemdata in data['lemmas'].values():
        lemdata['r'] = choose_representative(lemdata['w'])
