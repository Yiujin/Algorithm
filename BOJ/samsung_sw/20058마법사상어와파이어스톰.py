'''
A[r][c] = 0 -> 얼음 없음
(r,c)와 상하좌우 인접
파이어스톰 Q번 시전
1. 부분 격자로 나누기 -> 2^L , 단계마다 L = 1,2,3...
2. 모든 부분격자 시계방향 90도 회전
https://m.blog.naver.com/pasdfq/222120359076
3. 얼음이 있는 칸 3개이상과 인접해있지 않은 칸은 값 -1

Q번 이후
4. 남아있는 얼음 A[r][c]의 합
5. 남아있는 얼음중 가장 큰 덩어리가 차지하는 칸의 개수 -> bfs

'''
from collections import deque
def bfs(mat, visit, r, c):
    cnt2 = 1
    q = deque()
    q.append((r,c))
    visit[r][c] = 1
    while q:
        r,c = q.popleft()
        for i in range(4):
            tr = r+dr[i]
            tc = c+dc[i]
            if 0<=tr<N and 0<=tc<N and mat[tr][tc] >0 and visit[tr][tc] == 0:
                cnt2 += 1
                visit[tr][tc] = 1
                q.append((tr, tc))
    return cnt2

# main
N, Q = map(int, input().split())
N = 2**N
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for L in map(int, input().split()):
    # 1,2. devide and rotate
    k = 2**L
    for x in range(0, N, k):
        for y in range(0, N, k):
            tmp = [mat[i][y:y+k] for i in range(x, x+k)]
            # print(f' tmp : {tmp}')
            for i in range(k):
                for j in range(k):
                    mat[x+j][y+k-1-i] = tmp[i][j]

    # 3. 인접 얼음 # 상하좌우
    ice_cnt = [[0] *N for i in range(N)]
    for r in range(N):
        for c in range(N):
            cnt = 0
            for i in range(4):
                tr = r + dr[i]
                tc = c + dc[i]
                if 0<=tr<N and 0<=tc<N:
                    ice_cnt[r][c] += 1 if mat[tr][tc] > 0 else 0

    # for m in ice_cnt:
    #     print(m)

    # 얼음 제거
    for x in range(N):
        for y in range(N):
            if mat[x][y] >0 and ice_cnt[x][y] < 3:
                mat[x][y] -= 1

# 4. 남은 얼음 # 5. 제일 큰 덩어리
ans = [0,0]
visit = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if mat[i][j] > 0:
            ans[0] += mat[i][j] # 남은 얼음
            if visit[i][j] == 0: # 제일 큰 덩어리
                tmp = bfs(mat, visit, i, j)
                if tmp > ans[1]:
                    ans[1] = tmp

for a in ans:
    print(a)