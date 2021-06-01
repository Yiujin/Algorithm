import sys
answer =0 
def dfs(tp, N, day, tmp_cost):
    # 종료조건
    if day == N:
        global answer
        answer = max(tmp_cost, answer)
        # print(answer)
        return 

    # day에 일하는 경우
    if day + tp[day][0] <= N:
        dfs(tp, N, day + tp[day][0], tmp_cost + tp[day][1])

    # day에 일 안하는 경우 그냥 다음날로 넘어감
    if day + 1 <= N:
        dfs(tp, N, day+1, tmp_cost)


if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input())
    tp = []
    for i in range(N):
        t, p = map(int, input().split())
        tp.append([t,p])
    
    dfs(tp, N ,0, 0)
    print(answer)


