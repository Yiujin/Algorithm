'''
N번의 구슬, W : col, H : row
1. 1 ≤ N ≤ 4

2. 2 ≤ W ≤ 12

3. 2 ≤ H ≤ 15

최대한 많은 벽돌 제거하고
남은 벽돌의 수
1. 폭탄 터뜨리고
2. 행렬 내려오고
3. N 번만큼 1,2 반복

'''
def product(arr, r):
    # n번의 구슬 던지기 -> 중복 순열로 열 인덱스 가져오기
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr, r-1):
                yield [arr[i]] + next

from collections import deque
import copy
def bomb(mat, r,c):
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    q = deque()
    q.append((r,c, mat[r][c]))
    mat[r][c] = 0
    while q:
        r,c,value = q.popleft()
        for i in range(4):
            for s in range(1, value):
                tr = r + dr[i]*s
                tc = c + dc[i]*s
                if 0<=tr<row and 0<=tc<col:
                    if mat[tr][tc] > 1:
                        q.append((tr,tc,mat[tr][tc]))
                    mat[tr][tc] = 0

import re
def reset(arr,col,row):
    new = [[0] * col for _ in range(row)]
    tmp = []
    for line in zip(*arr):
        s = ''.join(map(str, line))
        s = re.sub(r'0', '', s)
        s = s.zfill(row)
        tmp.append(list(s))

    for i in range(row):
        for j in range(col):
            new[i][j] = int(tmp[j][i])

    return new

# main
T = int(input())
for tc in range(T):
    ans = 1e9
    N,col,row = map(int, input().split())
    mat = []
    for _ in range(row):
        mat.append(list(map(int, input().split())))

    arr = [i for i in range(col)]
    for prod in product(arr, N): # N개의 열을 포함하는 중복순열 / 이거 중에 제일 많이 터뜨리고 남은 벽돌갯수
        mat_b = [d[:] for d in mat]
        for j in prod: # 열
            for i in range(N):
                if mat_b[i][j] != 0:
                    bomb(mat_b,i,j)
                    # print('sfter bomb')
                    # for m in mat_b:
                    #     print(m)
                    mat_b = reset(mat_b, col,row)
                    # print('after reset')
                    # for m in mat_b:
                    #     print(m)
                    break
        print('every prod')
        for m in mat_b:
            print(m)

        # 남은 벽돌 갯수 제일 적은거
        tmp_ans = col*row
        for b in mat_b:
            tmp_ans -= b.count(0)
        ans = min(ans, tmp_ans)
    print(f'#{tc+1} {ans}')


