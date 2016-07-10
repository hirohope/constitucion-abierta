'''
input:
  'actaids': {'file1.txt': 1, 'file2.txt': 2, ...}
  'actaids.txt': 'file.txt'

output file:
  lines of the form "actaid    file.txt"
  (sorted by actaid)
'''
def export_actaids(data):
    actaids = data['actaids']
    actaids = sorted([(actaid, txt) for txt, actaid in actaids.items()])
    with open(data['actaids.txt'], 'w') as f:
        for actaid, txt in actaids:
            f.write("{}\t{}\n".format(actaid, txt))
