def solution(n): # 효율성 실패 
    if n <= 3:
        return '124'[n-1

    else:
        q,r = divmod(n-1, 3)
        return solution(q) + '124'[r]

if __name__ == "__main__":
    # n <= 500,000,000
    n = 1 # 1
    n = 2 # 2
    n = 3 # 4
    n = 4 # 11

    print(solution(9))