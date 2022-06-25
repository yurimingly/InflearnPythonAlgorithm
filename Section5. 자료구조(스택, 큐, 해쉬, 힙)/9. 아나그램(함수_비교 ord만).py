import sys
from collections import deque 
sys.stdin = open("input.txt", "r")

a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x,0) + 1
for x in b:
    str2[x] = str2.get(x,0) + 1

for i in str1.keys(): #여기에 있는 key값은
    if i in str2.keys(): #여기에도 있어야 한다.
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")