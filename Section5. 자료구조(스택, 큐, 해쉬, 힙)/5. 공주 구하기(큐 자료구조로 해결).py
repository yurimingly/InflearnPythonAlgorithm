import sys
from collections import deque 
sys.stdin = open("input.txt", "r")
#+  -  *  /  (  )

n, m = map(int,input().split())
Q = [(pos,val) for pos,val in enumerate(list(map(int,input().split())))]

print(Q)