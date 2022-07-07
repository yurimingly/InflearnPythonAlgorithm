#Section7. 깊이, 넓이 우선탐색 활용
#8. 송아지 찾기(BFS)
import sys
from collections import deque
sys.stdin=open("input.txt","r")

MAX = 1000000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int,input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ :
    now = dQ.popleft() #큐에서 하나 꺼내서

    if now==m:
        break

    for next in(now-1, now+1, now+5): #튜플값을 하나 하나 탐색
        if 0<next<=MAX:
            if ch[next]==0:#방문을 한건 넣으면 안됨
                dQ.append(next) #next를 넣어줌
                ch[next]=1      #방문했다
                dis[next]=dis[now]+1 #계속 뻗는다 = 자기부모+1
    
print(dis[m])