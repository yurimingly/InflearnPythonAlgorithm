import sys
sys.stdin = open("input.txt","rt")
a= list(range(21))
'''==같은 표현방식
n = list()
for i in range(1,21): n.append(i)'''

for _ in range(10):
    s,e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)#제일 앞에꺼 꺼낸다
#a.pop()#제일 뒤에꺼 꺼낸다

for x in a:
    print(x,end=' ')