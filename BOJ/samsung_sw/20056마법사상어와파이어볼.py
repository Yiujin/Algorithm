'''
https://www.acmicpc.net/problem/20056
1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
2-2. 파이어볼은 4개의 파이어볼로 나누어진다.
2-3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
4. 질량이 0인 파이어볼은 소멸되어 없어진다.

마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자


4 ≤ N ≤ 50
0 ≤ M ≤ N^2
1 ≤ K ≤ 1,000
1 ≤ ri, ci ≤ N
1 ≤ mi ≤ 1,000
1 ≤ si ≤ 1,000
0 ≤ di ≤ 7
'''

def move(mat, N, r, c):
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    trtc = []
    lm = len(mat[r][c])
    for _ in range(lm):
        (m,d,s,y) = mat[r][c][0]
        if y == 0:
            tr = (r + dr[d] * s) % N
            tc = (c + dc[d] * s) % N
            # print(f'{(m,d,s)} :  {r}, {c} -> {tr}, {tc}')
            mat[tr][tc].append((m,d,s,1))
            trtc.append((tr,tc))
            del mat[r][c][0]

        # print('after move')
        # for d in mat:
        #     print(d)

    return mat, trtc

def sum(mat, r,c):
    total = [0,0,0]
    lm = len(mat[r][c])
    for (m, d, s, y) in mat[r][c]:
        total[0] += m
        total[2] += s
        if d % 2 == 0: # 짝수면 0더하고 홀수면 1더해
            total[1] += 0
        else:
            total[1] += 1

    if total[1] == 0 or total[1] == lm:
        d = [0,2,4,6]
    else:
        d = [1,3,5,7]

    # print('total : ',total)
    mat[r][c] = []
    for i in range(4):
        mat[r][c].append((total[0] // 5,d[i],total[2] // lm, 0))

    return mat


from collections import deque
if __name__ == '__main__' :
    N,M,K = map(int, input().split()) # 격자크기, 파이어볼 갯수, 이동명령 수
    mat = [[[] for _ in range(N)] for _ in range(N)]
    noterc = []

    for _ in range(M):
        r,c,m,s,d = map(int, input().split())
        mat[r-1][c-1].append((m,d,s,0)) # 질량, 방향, 속력, 이동 여부
        noterc.append((r-1,c-1))

    # 이동 명령
    for k in range(K):
        # print(f'--------------{k+1}---------')
        # 이동
        new_noterc = []
        for (r,c) in noterc:
            if len(mat[r][c]) != 0:
                mat, trtc = move(mat,N, r,c)
                new_noterc.extend(trtc)

        # print(mat)
        new_noterc = list(set(new_noterc))
        # 2개 이상 합치기
        for (r,c) in new_noterc:
            if len(mat[r][c]) >= 2:
                mat = sum(mat, r,c)
            else:
                # print('while sum:', mat[r][c])
                (m,d,s,y) = mat[r][c][0]
                mat[r][c][0] = (m,d,s,0)

        # print('after sum : ')
        # for mm in mat:
        #     print(mm)
        noterc = new_noterc
        # print('noterc' , noterc)

    ans = 0
    for r,c in noterc:
        for (m,d,s, y) in mat[r][c]:
            ans += m
    print(ans)