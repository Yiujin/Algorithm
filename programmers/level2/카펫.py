import math

def solution(brown, yellow):
    answer=[]
    total= brown+yellow
    
    for col in range(1, total+1):
        if total % col == 0:
            row = total // col
            if row*2 + col*2 -4 == brown:
                if row >= col:
                    answer = [row, col]
                else: 
                    answer = [col, row]
    
    # print(answer)
    return answer

if __name__ == '__main__':
    br = [[10,2], [8,1], [24, 24]] #[4,3], [3,3, [8,6]

    for i in br:
        print(solution(i[0], i[1]))
