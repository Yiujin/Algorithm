import sys

input = sys.stdin.readline
N = int(input())
video = [list(map(int, input().strip())) for _ in range(N)]
# print(video)

result = ''
def quardtree(x ,y, n):
    global result
    check = video[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != video[i][j]: # 모두 같은 색이 아니면 쿼드 트리 호출
                result += '('
                quardtree(x,y,n//2) # 왼쪽 위
                quardtree(x,y+n//2,n//2) # 오른쪽 위
                quardtree(x+n//2,y,n//2) # 왼쪽 아래
                quardtree(x+n//2,y+n//2,n//2) # 오른쪽 아래
                result += ')'
                return result
    
    if check == 1:
        result += '1'
        return 
    else:
        result += '0'
        return
    
    # return result + ')'

quardtree(0,0,N)
print(result)

