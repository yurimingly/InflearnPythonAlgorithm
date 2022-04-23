import sys
sys.stdin = open("input.txt","rt")
n = int(input()) #input은 무조건 str로 읽는다
a = list(map(int,input().split()))
res = 0
tmp = 0

#쌤 방식
for x in a:
    if x==1:
        cnt+1
        sum+=cnt
    else:
        cnt=0
print(sum)

#내 방식
for idx, x in enumerate(a):
    if idx==0 and x==1:
        res+=1
    elif a[idx-1]==0 and x==1:
        tmp =1
        res += tmp
    elif a[idx-1]==1 and x==1:
        tmp +=1
        res += tmp
    elif x==0:
        tmp =0

print(res)