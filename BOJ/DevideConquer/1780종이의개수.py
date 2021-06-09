import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)

minus, zero, plus = 0,0,0
def dq9(x ,y, n):
    global minus, zero, plus
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                dq9(x, y, n//3) # (0,0)
                dq9(x, y+n//3, n//3) # (0,1)
                dq9(x, y+(n//3)*2, n//3) # (0,2)
                dq9(x+n//3, y, n//3) # (1,0)
                dq9(x+n//3, y+n//3, n//3) # (1,1)
                dq9(x+n//3, y+(n//3)*2, n//3)
                dq9(x+(n//3)*2, y, n//3)
                dq9(x+(n//3)*2, y+n//3, n//3)
                dq9(x+(n//3)*2, y+(n//3)*2, n//3) # (2,2)
                return
    
    if check == -1:
        minus += 1
        return
    elif check == 0:
        zero += 1
        return
    else:
        plus +=1
        return

dq9(0,0,N)
print(minus)
print(zero)
print(plus)
