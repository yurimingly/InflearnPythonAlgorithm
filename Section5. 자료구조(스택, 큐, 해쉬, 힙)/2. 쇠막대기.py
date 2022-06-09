import sys
sys.stdin = open("input.txt", "r")

s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else: #닫는괄호면
        if s[i-1] == '(': #레이저
            stack.pop()
            cnt += len(stack) #앞의 레이저막대기의 갯수
        else: #레이저가 아닌 쇠막대기의 끝
            stack.pop()
            cnt += 1

print(cnt)