import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())
horses = []
for i in xrange(N):
    horse = int(raw_input())
    horses.append(horse)
horses.sort()
min_diff = sum(horses)
for j in range(len(horses)-1):
    if abs(horses[j] - horses[j+1])<min_diff:
        min_diff = abs(horses[j] - horses[j+1])

print min_diff