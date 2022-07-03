#Section7. 깊이, 넓이 우선탐색 활용
#3.
import sys
sys.stdin=open("input.txt","r")

# keypoint!
# 

def DFS(L,sum):
    global res
    if L==n:
        if 0<sum<=s: #음수는 버려도 되니까
            res.add(sum)

    else:
        DFS(L+1,sum+G[L]) #추를 왼쪽에 놓는다.
        DFS(L+1,sum-G[L]) #추를 오른쪽에 놓는다.
        DFS(L+1,sum)      #추를 안놓는다

if __name__=="__main__":
    n = int(input())
    G= list(map(int,input().split()))
    s=sum(G)
    res=set() #1이 나오는 경우의 수, 1하고 다음추를 산정안하는 경우의 수 등등 같이 계산해야 되니까
    DFS(0,0)
    print(s-len(res)) #총 경우의 수 - 자료가 들어간 수, 그것을 빼면