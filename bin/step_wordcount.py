'''
input:
  'words': {'meaningful-word 1': {'p': [(actaid, wordindex), ...], ...},
            'meaningful-word 2': {'p': [(actaid, wordindex), ...], ...},
            ...}

output:
  'words': {'meaningful-word 1': {'c': count1, 'e': elas1...},
            'meaningful-word 2': {'c': count2, 'e': elas2...},
            ...}
'''
def add_wordcount(data):
    for worddata in data['words'].values():
        positions = worddata['p']
        worddata['c'] = len(positions)
        worddata['e'] = len(set([actaid for actaid, wordindex in positions]))
