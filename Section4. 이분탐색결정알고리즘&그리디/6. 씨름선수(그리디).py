import sys
sys.stdin = open("input.txt", "r")

n=int(input())
body = []
for i in range(n):
    s, e = map(int, input().split())
    body.append((s,e))

body.sort(key = lambda x : (x[0],x[1]), reverse=True)
largest = 0
cnt = 0

for h,w in body:    #height, weight
    if w > largest: #최대값이 갱신되는것
        largest = w
        cnt += 1
print(cnt)