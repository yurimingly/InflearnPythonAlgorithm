#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#11. 수들의 조합
import sys
sys.stdin=open("input.txt","r")

def DFS(b):
    global cnt
    if b==n:
        for x in path :
            print(x,end=' ')
        print()
        cnt+=1
    else:
        for branch in range(1,n+1): #방문하려는 노드 
            if g[b][branch] == 1 and ch[branch] ==0: #b에서 i로 넘어가야지
                ch[branch]=1
                path.append(branch)
                DFS(branch)
                path.pop()
                ch[branch]=0

if __name__=="__main__":
    n,m = map(int,input().split()) # 5 9
    g = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        g[a][b]=1

    ch = [0]*(n+1)
    ch[1]=1
    
    cnt=0
    path=[]
    path.append(1)
    DFS(1)
    print(cnt)
