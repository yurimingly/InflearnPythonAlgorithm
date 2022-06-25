import sys
sys.stdin = open("input.txt", "r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*n)
a.append([0]*n)

#0으로 초기화
for x in a:
    x.insert(0,0)
    x.append(0)

cnt = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)) : #k가 0~3될때까지 상하좌우 탐색 / all :  모두 참이라면
            cnt +=1
print(cnt)