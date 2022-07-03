#Section7. 깊이, 넓이 우선탐색 활용
#2. 휴가(삼성 SW역량평가 기출문제:DFS활용)
import sys
sys.stdin=open("input.txt","r")

def DFS(L,sum):
    global res
    if L == n+1:
        if res<sum:
            res=sum
    else:
        if L+pd[L]<=n+1: #현재날짜+상담할날짜 : 앞으로 뻗을 가지가 n+1보다 작아야..
            DFS(L+pd[L],sum+pm[L])
        DFS(L+1,sum)     #다음날짜로 진행

if __name__=="__main__":
    n = int(input())
    pd=[]
    pm=[]
    for _ in range(n):
        a,b = map(int,input().split())
        pd.append(a)
        pm.append(b)
    res=-2147000000

    pd.insert(0,0) #insert는 하나씩 밀리는 효과를 낸다.
    pm.insert(0,0)
    DFS(1,0)
    print(res)
