import codecs

def export_debug(data):
    with codecs.open(data['export-debug.py'], 'w', encoding='utf-8') as f:
        f.write(u"{}".format(data))
