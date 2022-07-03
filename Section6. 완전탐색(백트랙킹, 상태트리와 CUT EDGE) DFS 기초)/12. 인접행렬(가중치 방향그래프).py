#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#﻿12. 인접행렬(가중치 방향그래프)
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n,k = map(int,input().split())
g = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b,c = map(int,input().split())
    g[a][b] = c


for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end = ' ')

    print()

  
