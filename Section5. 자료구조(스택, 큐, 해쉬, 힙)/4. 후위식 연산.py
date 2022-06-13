import sys
sys.stdin = open("input.txt", "r")
#+  -  *  /  (  )
s = input()
stack = []
res = ''
tmp = 0

for i in s:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == '+':                
            tmp = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp + tmp1)
        elif i == '-':
            tmp = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp1 - tmp)
        elif i == '*':
            tmp = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp * tmp1)
        elif i == '/':
            tmp = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp / tmp1)

print(stack[0])