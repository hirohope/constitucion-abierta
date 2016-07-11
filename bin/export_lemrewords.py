import codecs
'''
input:
  'lemmas': {'lemma 1': {'c': cnt1, 'r': 're1', 'w': {'word1', 'word2', ...}},
             'lemma 2': {'c': cnt2, 'r': 're2', 'w': {'word1', 'word2', ...}},
            ...}

output file:
  lines of the form "lemma    representative    word1,word2,..."
  (sorted by freq)
'''
def export_lemrewords(data):
    items = [(ld['c'], L, ld['r'], ld['w']) for L, ld in data['lemmas'].items()]
    items.sort(reverse=True)
    with codecs.open(data['lemrewords.txt'], 'w', encoding='utf-8') as f:
        for count, lemma, representative, words in items:
            words = u','.join(sorted(list(words)))
            f.write(u"{}\t{}\t{}\n".format(lemma, representative, words))
