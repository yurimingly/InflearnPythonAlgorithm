import sys
from collections import deque 
sys.stdin = open("input.txt", "r")

a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x,0) + 1
for x in b:
    sH[x] = sH.get(x,0) - 1

for x in a:
    if sH.get(x)>0:
        print("NO")
else:
    print("YES")