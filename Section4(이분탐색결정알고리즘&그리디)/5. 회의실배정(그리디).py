import sys
sys.stdin = open("input.txt", "r")

n=int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1],x[0])) # x의 1번이 우선순위 / x의 0번이 뒷순서가 되도록 해라

et=0 #endtime
cnt=0
for s,e in meeting:  #시작시간s, 끝나는시간e
    if s >= et: #회의를 했으니까
        et = e
        cnt += 1

print(meeting)