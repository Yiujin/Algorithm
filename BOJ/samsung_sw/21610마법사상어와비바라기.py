
def move(A, N, d,s, chk):
    # c = n-1 : 오른쪽, 즉 열이 커지는 이동은 열을 0으로 : 4,5,6
    # c = 0 : 왼쪽, 즉 열이 작아지는 이동은 열을 n-1 로 : 1,2,8
    # r = n-1 : 아래쪽, 즉 행이 커지는 이동은 행을 0으로 : 6,7,8
    # r = 0 : 위쪽, 즉 행이 작아지는 이동은 행을 n-1 로 : 2,3,4

    # 다음 위치 = 현재위치 + (이동할 칸 수 % N)
    dxdy = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1],
            [0, 1], [1, 1], [1, 0], [1, -1]]
    new_chk = []
    # 구름 이동
    for r,c in chk:
        mv_r, mv_c = (dxdy[d][0] * s),(dxdy[d][1] * s)
        tr, tc = (r + mv_r) % N, (c + mv_c) % N
        # print('now : ', r,c, 'mv value : ', mv_r, mv_c, 'next : ', tr,tc, N)
        # 이동하고 나선 무조건 물 1 추가
        new_chk.append((tr,tc))
        A[tr][tc] += 1
    # print('이동 후 비내리고 난 후')
    # for i in A:
    #     print(i)
    # 1. 이전에 구름이 있던 칸을 제외한 나머지에서 -> x
    # 2. 대각선 물 유무에 따라 물 증가
    after_copy = A.copy()
    diag = [[-1,-1], [-1, 1], [1,-1], [1, 1]]
    for r,c in new_chk:
        # if (r, c) not in chk:  # 1
        for i,j in diag:
            # print(i, j)
            if 0 <= r+i < N and 0 <= c+j < N:
                if A[r+i][c+j] > 0: # 2
                    # print(A[r+i][c+j])
                    after_copy[r][c] += 1
    # print('after water copy')
    # for i in after_copy:
    #     print(i)

    return after_copy, new_chk

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
    # 1. 이전에 구름이 있던 칸을 제외한 나머지에서 -> x
    # 2. 대각선 물 유무에 따라 물 증가
    after_copy = A.copy()
    diag = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for r, c in new_chk:
        # if (r, c) not in chk:  # 1
        for i, j in diag:
            # print(i, j)
            if 0 <= r + i < N and 0 <= c + j < N:
                if A[r + i][c + j] > 0:  # 2
                    # print(A[r+i][c+j])
                    after_copy[r][c] += 1

if __name__ == '__main__':
    answer = 0
    ds = [0] * 9

    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    # chk = 구름 index
    chk = [ (N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
    # print(A)

    for i in range(M):
        # print(f'term :  {i}')
        d,s = map(int, input().split())
        A, chk = move(A, N, d, s, chk)
        # 1. 규름 있는 곳(chk) 제외 하고 모든곳에서
        # 2. 물의 양이 2이상이면 구름 생김
        final_chk = []
        for r in range(N):
            for c in range(N):
                if (r,c) not in chk and A[r][c] >=2 :
                    final_chk.append((r,c))

        # 구름 생긴 칸에 물 양 2 줄어듬
        for (r, c) in final_chk:
            A[r][c] -= 2
        chk = final_chk

        # print('물의양이 2 줄어들고 난 후')
        # for row in A:
        #     print(row)

    for row in A:
        answer += sum(row)
    print(answer)