from collections import defaultdict
from step_tokenize import meaningfulword_tokenize

'''
input:
  'txts': ['file1.txt', 'file2.txt', ..., 'fileN.txt']

output:
  'actaids': {'file1.txt': 1, 'file2.txt': 2, ...}
'''
def add_actaids(data):
    data['actaids'] = {}    
    for index, txt in enumerate(data['txts'], 1):
        data['actaids'][txt] = index


'''
input:
  'txts': ['file1.txt', 'file2.txt', ..., 'fileN.txt']
  'actaids': {'file1.txt': 1, 'file2.txt': 2, ...}
  'stop-words': {'stopword 1', 'stopword 2', ...}

output:
  'words': {'meaningful-word 1': {'p': [(actaid, wordindex), ...], ...},
            'meaningful-word 2': {'p': [(actaid, wordindex), ...], ...},
            ...}
'''
def add_wordpositions(data):
    data['words'] = defaultdict(lambda: {'p': []})
    words = data['words']
    actaids = data['actaids']
    stopwords = data['stop-words']
    for txt in data['txts']:
        tokens = meaningfulword_tokenize(txt, stopwords)
        actaid = actaids[txt]
        add_tokens_to_wordpositions(tokens, words, actaid)


# tokens = ['meaningful-word 1', 'meaningful-word 2', ...]
# words = {'meaningful-word 1': {'positions': [(actaid, wordindex), ...], ...},
#          'meaningful-word 2': {'positions': [(actaid, wordindex), ...], ...},
#          ...}
# actaid = int
#
def add_tokens_to_wordpositions(tokens, words, actaid):
    for index, word in enumerate(tokens):
        position = (actaid, index)
        words[word]['p'].append(position)
