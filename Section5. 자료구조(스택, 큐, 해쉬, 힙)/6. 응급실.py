import sys
from collections import deque 
sys.stdin = open("input.txt", "r")
#+  -  *  /  (  )

n, m = map(int,input().split())
Q = [(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
Q = deque(Q)
cnt = 0

while Q:
    cur = Q.popleft()
    if (cur[1] < x[1] for x in Q): #큐에 있는게 x보다 크면
        Q.append(cur)
    else: #이제 위험도 90짜리가 맨 앞에 왔따,,
        cnt+=1
        if cur[0] == m:
            print(cnt)
            break