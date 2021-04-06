def check(matrix, x,y,n): # check node that move to
    if x > n-1 or y > n-1:
        return False
    if matrix[x][y] != 0:
        return False
    return True

def solution(n):
    answer = []
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    dxdy = [[1,0], [0,1],[-1,-1]] #down, right, left-diag
    x, y, step = 0,0,0
    max_num = n*(n+1) //2
    for i in range(1,max_num+1):
        # print(x,y)
        matrix[x][y] = i
        if check(matrix, x +dxdy[step][0], y+dxdy[step][1],n)==False:
            step = (step+1)%3
        x += dxdy[step][0]
        y += dxdy[step][1] 
        # print(matrix)
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                answer.append(matrix[i][j] )
           
    return answer

if __name__ == '__main__':
    nn = [3,4,5,6]
    for n in nn:
        print(solution(n)) # [1,2,6,3,4,5], [1,2,9,3,10,8,4,5,6,7], [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9], 
                            # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]