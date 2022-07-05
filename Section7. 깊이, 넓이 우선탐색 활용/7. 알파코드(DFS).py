#Section7. 깊이, 넓이 우선탐색 활용
#
import sys
sys.stdin=open("input.txt","r")

def DFS(L,P):
    global cnt
    if L==n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+64), end = ' ')
        print()
    else:
        for i in range(1,27):
            if code[L]==i:
                res[P]=i
                DFS(L+1, P+1) #한자리 숫자일때
            elif i >= 10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                DFS(L+2,P+1) #두자리 숫자일때, p는 값을넣는 index니까

if __name__=="__main__":
    code=list(map(int,input()))
    n=len(code)
    code.insert(n,-1)##
    #25114라고 하면  code[L] == i//10 여기서 이미 걸려서 안넘어간다.
    ##25112라고 하면 근데 넘어가지만 넘어가서 list out of range에러난다.
    res = [0]*(n+3)
    cnt = 0
    DFS(0,0)
    print(cnt)
