#Section7. 깊이, 넓이 우선탐색 활용
#4.
import sys
sys.stdin=open("input.txt","r")

def DFS(L,sum):
    global cnt
    if sum > t:
        return
    if L==k: #동전의 갯수가 된다면
        if sum == t:
            cnt+=1
    else:
        for i in range(cn[L]+1): #cn의 L번째 동전
            DFS(L+1,sum+(cv[L]*i)) 

if __name__=="__main__":
    t = int(input())
    k = int(input())
    cv=[] #coinvalue
    cn=[]
    cnt=0
    for _ in range(k):
        a,b = map(int,input().split())
        cv.append(a)
        cn.append(b)

    DFS(0,0)
    print(cv)
    print(cn)
    print(cnt)