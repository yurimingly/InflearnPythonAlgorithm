import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())

cnt = [0]*(n+m+3) #n+m+3 갯수만큼 리스트의 크기가 생긴다.
max = -247000000

for i in range(1,n+1):
    for k in range(1,m+1):
        cnt[i+k] += 1

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i,end=' ')