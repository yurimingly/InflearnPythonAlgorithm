#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#8. 순열구하기
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def DFS(L):
    global cnt
    if L==m:
        for i in range(L):
           print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i #해당 레벨에서 i
                DFS(L+1)
                ch[i]=0
                

if __name__=="__main__":
    n,m = (map(int,input().split()))
    res=[0]*n
    ch = [0] * (n+1)
    cnt =0 
    DFS(0)
    print(cnt)