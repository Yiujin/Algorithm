import sys
import math

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    
    applicant = list(map(int, input().split()))
    # print(appliant)
    B, C = map(int, input().split())

    chk = False
    for i in applicant:
        if i > B: # 각 방의 지원자 수가 B보다 큰게 있으면 부감독관 필요
            chk = True
            break
    if not chk: #모든 지원자수가 B보다 작거나 같으면 총감독관만 있으면 됨
        # print("ff")
        print(N)
        exit(0)


    answer = N
    for i in applicant:
        if i > B:
            i -= B
            answer += math.ceil(i / C)

    print(answer)