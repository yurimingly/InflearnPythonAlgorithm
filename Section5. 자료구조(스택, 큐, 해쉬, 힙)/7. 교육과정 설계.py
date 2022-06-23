import sys
from collections import deque 
sys.stdin = open("input.txt", "r")
#+  -  *  /  (  )

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need) #dq = [CBA]
    for x in plan:   #plan = [CBDADE]
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
        else:
            if len(dq)==0: #현수의 커리큘럼 dq가 없으면
                print("#%d YES" %(i+1))
            else :
                print("#%d NO" %(i+1))