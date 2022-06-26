#Section6. 완전탐색(백트랙킹, 상태트리와 CUT EDGE) DFS 기초)
#4. 합이 같은 부분집합(DFS:아마존 인터뷰)
import sys
sys.stdin=open("input.txt","r")

def DFS(L,sum):
    if sum > total//2: #어차피 sum == (total-sum)이게 안맞을테니까 return시켜버림 시간복잡도down
        return
    if L==n:
        if sum == (total-sum): #total//2는 안됨 -> total이 11일 수 있으니까
            print("YES")
            sys.exit(0) #함수가 아닌 프로그램종료
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)

    DFS(0,0)
    print("NO")
    