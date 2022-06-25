import sys
from collections import deque 
sys.stdin = open("input.txt", "r")

a = input()
b = input()
str1 = [0]*52 #0번부터 52번까지
str2 = [0]*52 #0번부터 52번까지

for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1   # 아스키넘버를 65 ~ 90
    else: #소문자 a가 26번으로 해싱
        str1[ord(x)-71] += 1
for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1   # 아스키넘버를 65 ~ 90
    else: #소문자 a가 26번으로 해싱
        str2[ord(x)-71] += 1
for i in range(52):
    if str1[i] != str2[i] : #대문자갯수가 동일하냐
        print("NO")
        break
else: print("YES")