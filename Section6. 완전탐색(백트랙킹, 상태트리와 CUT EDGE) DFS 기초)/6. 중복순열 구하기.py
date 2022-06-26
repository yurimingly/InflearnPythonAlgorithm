#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#6. 중복순열 구하기
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def DFS(L):
    global cnt
    if L==M:
        for j in range(M):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,N+1):
            res[L]=i
            DFS(L+1)
        

if __name__ == "__main__":
    N,M = map(int,input().split())
    res = [0]*M
    cnt =0
    DFS(0)
    print(cnt)
    