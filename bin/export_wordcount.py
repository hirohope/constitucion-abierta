import codecs
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
    items = [(wd['c'], wd['e'], word) for word, wd in data['words'].items()]
    items.sort(reverse=True)
    items = [u'  "%s": {"count": %d, "elas": %d}' % (word, count, elas)
             for count, elas, word in items]
    js = u',\n'.join(items)
    js = u'var data = {\n%s\n};\n' % (js)
    with codecs.open(data['wordcount.js'], 'w', encoding='utf-8') as f:
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
    items = [(wd['c'], word) for word, wd in data['words'].items()]
    items.sort(reverse=True)
    with codecs.open(data['wordcount.txt'], 'w', encoding='utf-8') as f:
        for count, word in items:
            f.write(u"{} {}\n".format(count, word))
