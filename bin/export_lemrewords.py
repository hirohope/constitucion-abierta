import codecs
'''
input:
  'lemmas': {'lemma 1': {'r': 'representative1', 'w': {'word1', 'word2', ...}},
             'lemma 2': {'r': 'representative2', 'w': {'word1', 'word2', ...}},
            ...}

output file:
  lines of the form "lemma    representative    word1,word2,..."
  (sorted by lemma)
'''
def export_lemrewords(data):
    items = [(lemma, ld['r'], ld['w']) for lemma, ld in data['lemmas'].items()]
    items.sort()
    with codecs.open(data['lemrewords.txt'], 'w', encoding='utf-8') as f:
        for lemma, representative, words in items:
            words = u','.join(sorted(list(words)))
            f.write(u"{}\t{}\t{}\n".format(lemma, representative, words))
