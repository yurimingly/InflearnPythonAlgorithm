#Section7. 깊이, 넓이 우선탐색 활용
#5. 동전 분배하기(DFS)
import sys
sys.stdin=open("input.txt","r")

def DFS(L):
    global res
    if L==n:
        cha = max(money)-min(money)
        if res>cha:
            tmp = set() # money의 금액이 모두 달라야 한다.
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
        return
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]


if __name__=="__main__":
    n=int(input())
    coin = []
    money =[0]*3
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
