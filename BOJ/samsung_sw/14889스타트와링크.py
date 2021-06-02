import sys
from itertools import combinations

if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input())
    idx = [i for i in range(N)]
    s = []
    total = 0
    for i in range(N):
        input_ = list(map(int, input().split()))
        s.append(input_)
        total += sum(input_)

    team_com = list(combinations(idx , N// 2))
    team1 = team_com[:len(team_com)//2]
    # team2 = list(reversed([t for t in team_com if t not in team1]))
    # print(team1, team2)

    # 모든 조합의 경험치 차이 계산 
    min_v = 1000
    for t1 in team1:
        exp_com1 = list(combinations(t1, 2))
        # exp_com2 = list(combinations(t2, 2))
        # print(exp_com1, exp_com2)
        exp1, exp2 = 0,0
        for (a, b) in exp_com1:
            exp1 += s[a][b] + s[b][a]
            
        exp2 = total-exp1
        if abs(exp1 - exp2) < min_v:
            min_v = abs(exp1 - exp2)  
    print(f'min_V : {min_v}' )
    print(min_v)