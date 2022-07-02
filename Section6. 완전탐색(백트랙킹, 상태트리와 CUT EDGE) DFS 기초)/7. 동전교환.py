#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#7. 동전교환
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def DFS(L,sum):
    global res
    if L>res: #컷.. 최소보다 크면 더 구할 필요가 없다.
        return
    if sum>m:
        return
    if sum == m:
        if L<res: #res를 참조하니까 global res를 설정해줘야한다.
            res=L #값을 바꾸니까 지역변수인줄 알았는데
    else:
        for i in range(N):
            DFS(L+1,sum+a[i])

if __name__=="__main__":
    N=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    res=2147000000
    a.sort(reverse=True) #레벨 4까지가 4개가 최소라고 하면 그이상구할일이 없다.

    DFS(0,0)
    print(res)