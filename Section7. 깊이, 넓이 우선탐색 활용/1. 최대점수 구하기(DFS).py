#Section7. 깊이, 넓이 우선탐색 활용
#1.최대점수 구하기(DFS)
import sys
sys.stdin=open("input.txt","r")

def DFS(L,sum,time):
    global res
    if time > m:
        return
    if L==n:
        if res<sum:
            res=sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L])
        DFS(L+1,sum,time)


if __name__=="__main__":
    n,m = map(int,input().split()) # 5 20
    pv = list()
    pt = list()

    for _ in range(n):
        a,b= map(int,input().split()) 
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0,0,0)
    print(res)