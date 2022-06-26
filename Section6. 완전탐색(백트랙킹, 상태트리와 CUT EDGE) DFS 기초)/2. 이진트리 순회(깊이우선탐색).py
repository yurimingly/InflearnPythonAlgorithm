#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#2. 이진트리 순회(깊이우선탐색)
import sys

def DFS(v):
    if v>7:
        return
    else:
        print(v) #자기본연의 일을 하고 왼쪽 오른쪽가면 전위순회
        DFS(v*2)
        #print(v) #왼쪽갔다가 일을 하고 오른쪽가면 중위순회
        DFS(v*2+1)
        #print(v) #왼쪽갔다가 오른쪽가면 일을 하고 후위순회

if __name__ == "__main__":
    DFS(1)