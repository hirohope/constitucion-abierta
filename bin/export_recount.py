import codecs
'''
input:
  'lemmas': {'lemma 1': {'r': 'representative1', 'c': count1, 'e': elas1...},
             'lemma 2': {'r': 'representative2', 'c': count2, 'e': elas2...},
            ...}

output file:
  javascript of the form:
  var data = {
    "representative1": {"count": count1, "elas": elas1},
    "representative2": {"count": count2, "elas": elas2},
    ...
  };
'''
def export_recount_json(data):
    items = [(ld['c'], ld['e'], ld['r']) for ld in data['lemmas'].values()]
    items.sort(reverse=True)
    items = [u'  "%s": {"count": %d, "elas": %d}' % (word, count, elas)
             for count, elas, word in items]
    js = u',\n'.join(items)
    js = u'var data = {\n%s\n};\n' % (js)
    with codecs.open(data['wordcount.js'], 'w', encoding='utf-8') as f:
        f.write(js)

'''
input:
  'lemmas': {'lemma 1': {'r': 'representative1', 'c': count1},
             'lemma 2': {'r': 'representative2', 'c': count2},
            ...}

output file:
  lines of the form "count representative"  
'''
def export_recount_txt(data):
    items = [(ld['c'], ld['r']) for ld in data['lemmas'].values()]
    items.sort(reverse=True)
    with codecs.open(data['wordcount.txt'], 'w', encoding='utf-8') as f:
        for count, word in items:
            f.write(u"{} {}\n".format(count, word))
