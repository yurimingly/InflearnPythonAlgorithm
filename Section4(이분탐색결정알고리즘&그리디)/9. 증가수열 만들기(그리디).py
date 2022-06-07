import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int,input().split()))
res = ""
#index
lt = 0
rt = n-1

last = 0
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt],'R'))
    tmp.sort() # 튜플의 첫자료값에 의해 정렬
    if len(tmp) ==0: #더이상가져올 수 없을때
        break
    else: # if a[lt] > last: 또는 if a[rt] > last: 를 타고 tmp에 적재가 된게 끝났을때
        res = res+tmp[0][1] #제일앞의 자료의 'L' 또는 'R'
        last = tmp[0][0] #제일 앞 자료의 숫자
        if tmp[0][1] == 'L': #왼쪽에서 들어가면 
            lt += 1 #하나증가시켜서 좁혀준
        else:
            rt -= 1 #하나증가시켜서 좁혀준
    tmp.clear()

print(len(res))
print(res)