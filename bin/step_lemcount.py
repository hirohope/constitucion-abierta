'''
input:
  'lemmas': {'lemma 1': {'p': [(actaid, wordindex), ...], ...},
             'lemma 2': {'p': [(actaid, wordindex), ...], ...},
             ...}

output:
  'lemmas': {'lemma 1': {'c': count1, 'e': elas1},
             'lemma 2': {'c': count2, 'e': elas2},
             ...}
'''
def add_lemcount(data):
    for lemdata in data['lemmas'].values():
        positions = lemdata['p']
        lemdata['c'] = len(positions)
        lemdata['e'] = len(set([actaid for actaid, wordindex in positions]))
