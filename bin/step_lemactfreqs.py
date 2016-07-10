from collections import defaultdict

'''
input:
  'lemmas': {'lemma 1': {'p': [pos11, pos12, ...], ...},
             'lemma 2': {'p': [pos21, pos22, ...], ...},
             ...}

output:
  'lemmas': {'lemma 1': {'a': {actaid11: freq11, actaid12: freq12, ...}, ...},
             'lemma 2': {'a': {actaid21: freq21, actaid22: freq22, ...}, ...},
             ...}
'''
def add_lemactfreqs(data):
    for lemdata in data['lemmas'].values():
        add_actfreqs_to_lemdata(lemdata)
        
def add_actfreqs_to_lemdata(lemdata):
    lemdata['a'] = defaultdict(int)
    actfreqs = lemdata['a']
    positions = lemdata['p']
    for actaid, wordindex in positions:
        actfreqs[actaid] += 1
