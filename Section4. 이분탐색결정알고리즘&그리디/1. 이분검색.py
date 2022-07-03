import sys
sys.stdin = open("input.txt", "r")
n,m = map(int,input().split())
a=list(map(int,input().split()))
a.sort()
lt = 0
rt = n-1 #오른쪽 맨끝index

while lt<=rt:
    mid = (lt+rt)//2
    if m<a[mid]:
        rt=mid-1   #-1을 잊지말자
    elif m>a[mid]:
        lt=mid+1   #+1을 잊지말자
    else:
        print(mid+1)
        break