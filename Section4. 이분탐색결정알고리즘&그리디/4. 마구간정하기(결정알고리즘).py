import sys
sys.stdin = open("input.txt", "r")

def Count(capa):
    cnt = 1
    flag = line[0]
    for x in line:
        if x-flag >= capa: #현재내가 말을 배치하려는 위치 - 마구간의 처음 >= capa
            cnt += 1
            flag = x
        else:
            continue
    return cnt

N,C = map(int, input().split())
line = []
for _ in range(N):
    tmp = int(input())
    line.append(tmp)
line.sort()
lt = line[0];
rt = line[N-1];

while lt <= rt:
    mid = (rt+lt)//2
    if Count(mid) < C:
        rt = mid-1
        lt = line[0]
    if Count(mid) >= C: #큰거니까 성공할때
        res = mid
        lt = mid+1

print(res)