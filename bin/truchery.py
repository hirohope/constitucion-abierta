'''
requires:
  'words': {'meaningful-word 1': {'L': 'lemma1', ...},
            'meaningful-word 2': {'L': 'lemma2', ...}, ...}
'''
def trans_truchery(data):
    words = data['words']
    for word in words:
        words[word]['L'] = lemma_truch(words[word]['L'])

def lemma_truch(lemma):
    def fooblah(lemma, fooLen, blah):
        blahLen = len(blah)
        if len(lemma)-blahLen >= fooLen and lemma[-blahLen:] == blah:
            lemma = lemma[:-blahLen]
        return lemma
    def blahfoo(lemma, blah, newLemma):
        blahLen = len(blah)
        if len(lemma)-blahLen >= 3 and lemma[:blahLen] == blah:
            lemma = newLemma
        return lemma
    lemma = fooblah(lemma, 4, 'izacion')
    lemma = fooblah(lemma, 3, 'acion')
    lemma = fooblah(lemma, 6, 'iz')
    lemma = fooblah(lemma, 3, 'ed')
    lemma = fooblah(lemma, 3, 'ari')
    lemma = fooblah(lemma, 6, 'al')
    lemma = fooblah(lemma, 3, 'i')
    lemma = blahfoo(lemma, 'gobi', 'gob')
    lemma = blahfoo(lemma, 'democ', 'democ')
    if len(lemma) >= 6 and lemma[:6] == 'protec' or lemma[:6] == 'proteg':
        lemma = 'protex'
    return lemma
