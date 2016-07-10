'''
input:
output:
  'lemmas': {'lemma 1': {'a': {actaid11: freq11, actaid12: freq12, ...}, ...},
             'lemma 2': {'a': {actaid21: freq21, actaid22: freq22, ...}, ...},
             ...}
  'matrix.txt': 'file.txt'
  
output file:
  lines of the form "lemma: actaid1*freq1 actaid2*freq2 ..."
  (sorted by lemmas, then sorted by actaids)
'''
def export_matrix(data):
    lemmas = sorted(data['lemmas'].items())
    with open(data['matrix.txt'], 'w') as f:
        for lemma, lemdata in lemmas:
            actfreqs = sorted(lemdata['a'].items())
            actfreqs = ["%d*%d" % actfreq for actfreq in actfreqs]
            actfreqs = ' '.join(actfreqs)
            f.write("{}: {}\n".format(lemma, actfreqs))
