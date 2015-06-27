import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # Number of elements which make up the association table.
Q = int(raw_input()) # Number Q of file names to be analyzed.
extensions = dict()
for i in xrange(N):
    # EXT: file extension
    # MT: MIME type.
    EXT, MT = raw_input().split()
    extensions[EXT.lower()] = MT
for i in xrange(Q):
    FNAME = raw_input() # One file name per line.
    morceaux = FNAME.split(".")
    if len(morceaux) == 1:
        print "UNKNOWN"
    elif morceaux[len(morceaux)-1].lower() in extensions.keys():
        print extensions[morceaux[len(morceaux)-1].lower()]
    else:
        print "UNKNOWN"

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
