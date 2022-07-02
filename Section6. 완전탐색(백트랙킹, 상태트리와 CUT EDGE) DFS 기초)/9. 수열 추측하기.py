#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#9. 수열 추측하기
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def DFS(L,sum):
    global ch
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__=="__main__":
    n,f = map(int,input().split())
    p=[0]*n
    b=[1]*n
    cnt=0
    ch=[0]*(n+1)
    for i in range(1,n):
       b[i] = b[i-1]*(n-i)//i   #/i로 하면 소숫점 자리가 나온다.
    DFS(0,0)