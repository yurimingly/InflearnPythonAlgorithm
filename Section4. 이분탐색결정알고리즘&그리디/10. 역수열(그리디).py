import sys
sys.stdin = open("input.txt", "r")

N = int(input())
a = list(map(int,input().split()))
seq = [0]*N

for i in range(N):
    for j in range(N):
        if a[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1

for i in seq:
    print(i, end=' ')