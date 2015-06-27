import sys, math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(raw_input())
H = int(raw_input())
T = raw_input()
ROW = []
for i in xrange(H):
    ROW.append(raw_input())
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
def char_position(letter):
    r = ord(letter) - 97
    if r < 0 or r > 25:
        return 26
    else:
        return r
lignes = []
for k in range(H):
    lignes.append("")
for i in range(len(T)):
    for k in range(H):
        for j in range(L):
            lignes[k] += ROW[k][char_position(T[i].lower())*L+j]
for k in range(H):
    print "".join(lignes[k])
