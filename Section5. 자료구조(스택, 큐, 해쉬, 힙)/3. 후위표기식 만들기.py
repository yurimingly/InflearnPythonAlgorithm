import sys
sys.stdin = open("input.txt", "r")
#+  -  *  /  (  )
s = input()
stack = []
res = ''

for i in range(len(s)):
    if s[i].isdecimal():
        res += s[i]
    else :
        if s[i]=='(':
            stack.append(s[i])

        elif s[i]=='*' or s[i] == '/' :
            while stack and (stack[-1]=='*' or stack[-1]=='/'): #우선순위가 같으니까 먼저 꺼내야 한다.
                res += stack.pop()
            stack.append(s[i])

        elif s[i] == '+' or s[i] == '-': 
            while stack and stack[-1] != '(': #여는 괄호 속에 있는 +와 -
                res += stack.pop()
            stack.append(s[i])

        elif s[i]==')':
            while stack and stack[-1] != '(': #닫는 괄호 전에 있는 거 다 append
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)