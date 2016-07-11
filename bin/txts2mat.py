import glob, os, re
from step_lemmas import add_lemmas
from step_lempositions import add_lempositions
from step_lemactfreqs import add_lemactfreqs
from step_lemwords import add_lemwords
from step_lemcount import add_lemcount
from step_representatives import add_lemrepresentatives
from step_wordpositions import add_actaids, add_wordpositions
from step_wordcount import add_wordcount
from step_stopwords import add_stopwords, add_nostopwords
from truchery import trans_truchery
from export_matrix import export_matrix
from export_actaids import export_actaids
#from export_wordcount import export_wordcount_json, export_wordcount_txt
from export_recount import export_recount_json, export_recount_txt
from export_lemrewords import export_lemrewords
from functions_cli import *

def add_defaults(data):
    scriptpath = os.getcwd()
    data['stop-words.txt'] = os.path.join(scriptpath, 'stop-words.txt')
    data['no-stop-words.txt'] = os.path.join(scriptpath, 'no-stop-words.txt')
    data['matrix.txt'] = 'matrix.txt'
    data['actaids.txt'] = 'actaids.txt'
    data['wordcount.js'] = 'wordcount.js'
    data['wordcount.txt'] = 'wordcount.txt'
    data['lemrewords.txt'] = 'lemrewords.txt'

def add_txts(data):
    if not os.path.isdir(data['txts-path']):
        error_then_exit("argument is not an existing directory")
    os.chdir(data['txts-path'])
    txts = glob.glob('*.txt')
    data['txts'] = filter(txt_is_acta, txts)

def txt_is_acta(txt):
    return bool(re.match('[0-9A-Fa-f]+.txt', txt)) or \
           bool(re.match('[a-z]+[0-9]+.txt', txt))

data = {}
add_arguments(data)
add_defaults(data)
add_txts(data)
add_stopwords(data)
add_nostopwords(data)
add_actaids(data)
add_wordpositions(data)
add_wordcount(data)
add_lemmas(data)
trans_truchery(data)
add_lempositions(data)
add_lemactfreqs(data)
add_lemwords(data)
add_lemrepresentatives(data)
add_lemcount(data)

export_actaids(data)
#export_wordcount_json(data)
#export_wordcount_txt(data)
export_recount_json(data)
export_recount_txt(data)
export_matrix(data)
export_lemrewords(data)
