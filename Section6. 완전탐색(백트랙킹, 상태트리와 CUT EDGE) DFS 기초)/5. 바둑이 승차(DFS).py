#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#5. 바둑이 승차(DFS)
import sys
sys.stdin=open("input.txt","r")

def DFS(L,sum, tsum):
    global result
    if sum + (total-tsum) < result:
#(지금까지의 부분집합의 합 - #total-tsum 앞으로 판단해야할 바둑이의 값)
        return
    if sum>C:
        return
    if L==N:
        if result<sum:
            result=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])     #sum에 a[L]를 부분집합으로 참여시키지 않겠다.

if __name__ == "__main__":
    C,N = map(int,input().split())
    a=[0]*N
    result = -21470000000
    for i in range(N):
        a[i]=int(input())

    total = sum(a)
    DFS(0,0,0)
    print(result)