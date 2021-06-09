import sys

def paper_sum(paper):
    n = len(paper)
    tot = 0
    for i in range(n):
        tot += sum(paper[i])
    return tot

def dq(paper, n):
    global blue, white
    # print(f'front dq blue: {blue}, white: {white}')

    if paper_sum(paper) == n*n:
        blue += 1
        return
    if paper_sum(paper) == 0:
        white += 1
        return
    
    nn = n//2
    total1, total2, total3, total4 = [], [], [], []
    for i in range(nn): # 위에 두 조각의 각 합
        total1.append(paper[i][:nn])
        total2.append(paper[i][nn:n])
    for i in range(nn,n): # 아래 두조각 합
        total3.append(paper[i][:nn])
        total4.append(paper[i][nn:n])
    # print(total1, total2, total3, total4)
    dq(total1, nn)
    dq(total2, nn)
    dq(total3, nn)
    dq(total4, nn)
    return
    


if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    # print(paper)

    white , blue = 0, 0
    dq(paper, N)
    print(white)
    print(blue)
