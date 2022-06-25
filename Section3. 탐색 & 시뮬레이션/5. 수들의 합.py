import sys
sys.stdin = open("input.txt","rt")
#길이n#합m
n,m = map(int,input().split())
a = list(map(int, input().split()))

lt = 0 #왼쪽부터의 자리
rt = 1 #오른쪽부터의 자리
tot = a[0]
cnt=0

while True:
    if tot < m: #tot이 m(구해야하는total)보다 작을때
        if rt < n: #오른쪽부터의 자리가 총길이를 넘지 않을때
            tot += a[rt]
            rt += 1
        else : #n보다 클때 == 있을 수 없는 일이다. 가리키고 있는 자리수가 전체자리보다 크다니
            break
    elif tot == m: #total이 m과 같을때
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)