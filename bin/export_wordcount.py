'''
input:
  'words': {'meaningful-word 1': {'c': count1, 'e': elas1...},
            'meaningful-word 2': {'c': count2, 'e': elas2...},
            ...}

output file:
  javascript of the form:
  var data = {
    "meaningful-word1": {"count": count1, "elas": elas1},
    "meaningful-word2": {"count": count2, "elas": elas2},
    ...
  };
'''
def export_wordcount_json(data):
    items = ['  "%s": {"count": %d, "elas": %d}' % (word, wd['c'], wd['e'])
             for word, wd in data['words'].items()]
    js = ',\n'.join(items)
    js = 'var data = {\n%s\n};\n' % (js)
    with open(data['wordcount.js'], 'w') as f:
        f.write(js)

'''
input:
  'words': {'meaningful-word 1': {'c': count1, 'e': elas1...},
            'meaningful-word 2': {'c': count2, 'e': elas2...},
            ...}

output file:
  lines of the form "count meaningful-word"  
'''
def export_wordcount_txt(data):
    with open(data['wordcount.txt'], 'w') as f:
        for word, worddata in data['words'].items():
            f.write("{} {}\n".format(worddata['c'], word))
