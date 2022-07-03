#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#11. 수들의 조합
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def DFS(L,b,sum): #Level, branch,sum
    global cnt
    if L==k:
        if sum % m == 0:
            cnt+=1
    else:
        for i in range(b,n):
            DFS(L+1,i+1,sum+line[i])

if __name__=="__main__":
    n,k = map(int,input().split())
    line = list(map(int,input().split()))
    m=int(input())

    cnt=0
    DFS(0,0,0)
    print(cnt)