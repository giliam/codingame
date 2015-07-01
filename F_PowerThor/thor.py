import sys, math
LX, LY, TX, TY = [int(i) for i in raw_input().split()]
while 1:
    E = int(raw_input())
    display = ""
    if LY < TY:
        display += "N"
        TY -= 1
    elif LY > TY:
        display += "S"
        TY += 1
    if LX < TX:
        display += "W"
        TX -= 1
    elif LX > TX:
        display += "E"
        TX += 1
    print display