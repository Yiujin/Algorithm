answer = 0
ds = [0] * 9

N,M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
# chk = 구름 index
chk = [ (N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
# print(A)

def move():
    # 다음 위치 = 현재위치 + (이동할 칸 수 % N)
    dxdy = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1],
            [0, 1], [1, 1], [1, 0], [1, -1]]
    new_chk = []
    # 구름 이동
    for r, c in chk:
        mv_r, mv_c = (dxdy[d][0] * s), (dxdy[d][1] * s)
        tr, tc = (r + mv_r) % N, (c + mv_c) % N
        # print('now : ', r,c, 'mv value : ', mv_r, mv_c, 'next : ', tr,tc, N)
        # 이동하고 나선 무조건 물 1 추가
        new_chk.append((tr, tc))
        A[tr][tc] += 1
    # print('이동 후 비내리고 난 후')
    # for i in A:
    #     print(i)


def copy_water():
    # 2. 대각선 물 유무에 따라 물 증가
    after_copy = A.copy()
    diag = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for r, c in new_chk:
        for i, j in diag:
            # print(i, j)
            if 0 <= r + i < N and 0 <= c + j < N:
                if A[r + i][c + j] > 0:  # 2
                    # print(A[r+i][c+j])
                    after_copy[r][c] += 1