def choose_representative(words):
    return max(words, key=truchscore)

def truchscore(word):
    if word[-3:]=='nia': return (1001, 1001)
    return (len(word), charscore(word[-1]))

def charscore(c):
    if c == 'o': return 1000
    if c == 's': return 999
    if c == 'n': return 998
    return -ord(c)
