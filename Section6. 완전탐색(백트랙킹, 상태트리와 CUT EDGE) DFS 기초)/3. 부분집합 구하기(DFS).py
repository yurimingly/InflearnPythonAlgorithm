#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#3. 부분집합 구하기(DFS)

def DFS(v):
    if v==n+1:
        for i in range(1,n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=3
    ch=[0]*(n+1)
    DFS(1)
