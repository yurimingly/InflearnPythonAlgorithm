import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N,M = map(int,input().split())
p = list(map(int,input().split()))
p.sort()

p = deque(p)

cnt = 0
while p:
    if len(p) == 1:     #만약 1명만 남았다고 하면
        cnt +=1
        break
    if p[0]+p[-1] > M:
        p.pop()         #구명보트타고 탈출
        cnt+=1
    else :
        p.popleft() #######################변화된부분########################
        p.pop()
        cnt+=1

    if len(p)==0:
        break

print(cnt)