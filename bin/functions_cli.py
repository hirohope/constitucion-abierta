import sys

def error_then_exit(error):
    print "error: {}".format(error)
    print "process exited with error"
    sys.exit(1)

def usage_then_exit():
    print "usage: txts2mat.py path/to/dir"
    print "output: mat.txt"
    sys.exit(1)

def add_arguments(data):   
    args = sys.argv[1:]
    if len(args) == 0:
        usage_then_exit()
    if len(args) > 1:
        print "error: too many arguments"
        usage_then_exit()
    data['txts-path'] = args[0]
