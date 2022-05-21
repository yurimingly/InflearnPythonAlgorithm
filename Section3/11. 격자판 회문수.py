import sys
sys.stdin = open("input.txt", "r")
board = [list(map(int,input().split())) for _ in range(7)]
cnt =0

for i in range(3): #i=0과 1과 2
    for j in range(7): #행은 이렇게 슬라이스 이용가능하나
        tmp = board[j][i:i+5]#마지막 5까지안하고 4까지만 slice함
        if tmp==tmp[::-1] : #거꾸로
            cnt += 1
        for k in range(2): #열은 안된다. 포문써야됨. k=0과 1
            if board[i+k][j] != board[i+5-k-1][j]:
                break
            else:
                cnt += 1
print(cnt)