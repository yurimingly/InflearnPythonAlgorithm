import sys
sys.stdin = open("input.txt", "r")

def Count(capacity): #capa=mid
    cnt=1
    sum=0 #dvd에 저장되는 노래들을 합
    for x in Music:
        if sum + x > capacity: #새로운 노래를 저장할때 용량을 초과했으면
            cnt += 1          
            sum = x          
        else:
            sum += x
    return cnt

n,m=map(int,input().split())
Music = list(map(int,input().split()))
maxx = max(Music)
lt = 1
rt = sum(Music) #sum임을 기억할것!!!!!!!
res = 0

while lt <= rt:
    mid=(lt+rt)//2 #dvd 한 장의 용량
    if mid>=maxx and Count(mid) <= m: #dvd함수가 몇 장 필요하냐하는 함수 <= m(몇 장 필요한 함수)
    #dvd하나의 용량이 같거나 크다. 노래중에서 가장긴노래보다는.
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)