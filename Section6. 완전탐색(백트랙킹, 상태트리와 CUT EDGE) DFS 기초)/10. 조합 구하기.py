#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#10. 조합 구하기
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def DFS(L,b): #Level, branch 레벨과 가지
    global cnt
    if L==m:
        for i in range(m):
            if res[i]!=0:
                print(res[i], end=' ')
        cnt += 1
        print()
        return
    else:
        for i in range(b,n+1):
            res[L]=i
            DFS(L+1, i+1) #가지에다가 +1해줘야한다.

if __name__=="__main__":
    n,m = map(int,input().split())
    res = [0] *(n+1)
    cnt = 0
    DFS(0,1)
    print(cnt)