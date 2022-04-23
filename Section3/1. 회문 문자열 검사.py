import sys
sys.stdin = open("input.txt","rt")
n = int(input()) #input은 무조건 str로 읽는다

#첫번째 방법
for i in range(n):
    s=input()
    s=s.upper() #다 대문자로 맞춤
    size=len(s) #문자열의 길이 
    
    for j in range(size//2):
        if s[j] != s[-1-j]: #앞이랑 뒤랑 같으냐 ex. j==0이면 s[0]==s[-1]
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

#두번째 방법 파이썬스럽게
for i in range(n):
    s=input()
    s == s.upper()
    
    if s == s[::1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))