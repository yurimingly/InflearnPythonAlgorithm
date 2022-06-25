import sys
import heapq as hq
sys.stdin=open("input.txt","r")
a=[]

while True:
    n=int(input())
    if n == -1: #입력이 종료되는 거니까 끝
        break
    if n == 0: #heap의 root노드를 하나 찍어야하는디
        if len(a)==0: #힙에 아무것도 없다면
            print(-1)
        else:
            print(hq.heappop(a)) #root노드의 제일 작은 값을 꺼내줌
    else: #0이 아니면 어떤 숫자니까 그 값을 push해줌
        hq.heappush(a,n) #a라는 리스트에 n값을 push