import sys
sys.stdin = open("input.txt","rt")

a = input()
b,c,d = map(int,input().split())

#첫번째방법
def digit_sum(x):
    sum = 0
    while x > 0:
        sum+=x%10
        x=x//10
    return sum

#두번째방법 : string을 이용
def digit_sum(x):
    sum=0
    for i in str(x): #문자가 됨 print(i) 1 2 5 not 125
        sum += int(i) 
    return sum


max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)