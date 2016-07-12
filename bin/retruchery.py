from functions_txts import word_simplify

def choose_representative(data, words):
    lemcorrections = data['lemcorrections']
    return max(words, key=lambda word: truchscore(lemcorrections, word))

def truchscore(lemcorrections, word):
    if word in lemcorrections or '*'+word in lemcorrections: return (99999, 0)
    s = word_simplify(word)
    if s == "politica": return (10001, 0)
    if s[-3:]=='nia'  : return (10000, 0)
    if s[-4:]=='cion' : return ( 9999, 0)
    if s[-5:]=='mente': return (-9999, 0)
    if s[-3:]=='ndo'  : return (-9998, 0)
    return (len(s), charscore(s[-1]))

def charscore(c):
    if c == 'o': return 1000
    if c == 's': return 999
    if c == 'n': return 998
    return -ord(c)
