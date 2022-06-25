#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#1. 재귀함수를 이용한 이진수 출력
import sys
sys.stdin=open("input.txt","r")

def DFS(x):
    if x==0:
        return #함수를 종료시켜라
    else:
        print(x%2,end=' ') #나머지
        DFS(x//2) #몫

if __name__ == "__main__":
    x=int(input())
    DFS(x)