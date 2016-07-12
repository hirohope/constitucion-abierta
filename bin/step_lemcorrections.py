from functions_txts import read_contents
'''
input:
  'lemcorrections.txt': 'file.txt' (lines of the form "re    word1,word2,...")

output:
  'lemcorrections': {'representative1': {'word1', 'word2', ...}}
'''
def add_lemcorrections(data):
    filename = data['lemcorrections.txt']
    lemcorrections = {}
    lines = read_contents(filename).splitlines()
    for line in lines:
        line = line.split()
        if len(line) == 1: line.append('')
        if len(line) != 2: exit_with_error('bad line in {}'.format(filename))
        representative, words = line[0], set(line[1].split(','))
        words.discard('')
        lemcorrections[representative] = words
    data['lemcorrections'] = lemcorrections
