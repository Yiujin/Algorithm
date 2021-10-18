# 구슬 : 1,2,3
# 방향 : 위, 아래, 왼, 오 : 1,2,3,4
# 1. 마법 폭발:  방향 d, 거리 s -> 거리 s이하까지 구슬 폭발
# 2. 폭발 후 빈칸 생기면 구슬 이동 -> 다음 칸에 있는 구슬 앞으로 땡겨와
# 3. 연속 폭발 : 4개 이상 연속되면 폭발 -> 빈칸
# 4. 구슬 이동
# 5. 연속 폭발 : 폭발 -> 이동 반복 (연속 폭발 없을 떄까지)

# 6. 구슬 변화 : 연속 구슬 (갯수A, 변화B) -> 2칸씩

N,M = map(int, input().split())
answer = [0] * 4

mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))

# 초기 상어 위치
shark = (N+1)//2 -1

# 행렬 번호 배열 : 오-아-왼-우ㅣ
mv = [[0,1], [1,0], [0,-1], [-1,0]]
num_mat = [[0 for _ in range(N)] for _ in range(N)]
number = N*N -1
x, y = 0,0
step = 4
def check(num_mat, x,y,N):
    if 0 <= x < N and 0 <= y < N and num_mat[x][y] == 0:
        return True
    return False

for n in range(number, 0, -1):
    num_mat[x][y] = n
    if check(num_mat, x+mv[step%4][0], y+mv[step%4][1], N) == False:
        step+=1

    x+=mv[step%4][0]
    y+=mv[step%4][1]
    # print(x,y)


# 마법 방향
magic_direct = [[0,0], [-1,0], [1,0], [0,-1], [0,1]] # _, 위, 아래, 왼, 오

def blizard_explode(shark, d,s):
    p_ind = []
    rng = magic_direct[d] * s # ex) 3,0
    for i in range(1, s+1):
        drdc = [magic_direct[d][0] * i, magic_direct[d][1] * i]
        print(drdc)
        print(shark+drdc[0], shark+drdc[1])
        mat[shark+drdc[0]][shark+drdc[1]] = 0
        answer[mat[shark+drdc[0]][shark+drdc[1]]] += 1 # 폭발한 구슬 개수 세기
        p_ind.append((shark+drdc[0], shark+drdc[1]))
    return p_ind

def move(p_ind):
    stride = 1
    p_num = [num_mat[pi][pj] for (pi, pj) in p_ind] # 폭발한 애 번호
    # 1 <- 2 ~  폭발 <- 폭발한애 + 1
    for i in range(len(p_num)): # 이동 반복 횟수
        for n in range(1, p_num[i]+1):
            r,c = num_mat.index(n)
            tr, tc = num_mat.index(n + stride)
            mat[r][c] = mat[tr][tc]

        stride += 1

def move2(p_ind):
    # 1. 1차원으로 만들고
    # 2. 구슬 앞으로 이동
    # 3. 다시 2차원으로 만들기
    drdc = [[1,0], [0,1], [-1,0], [0,-1]] # 아 오 위 왼
    d1 = []
    # 1.
    for n in range(1, number):
        for ri, row in enumerate(num_mat):
            if n in row:
                r, c = ri, row.index(n)
        if mat[r][c] != 0: # 2.
            d1.append(mat[r][c])

    d1.extend([0]* (number-len(d1)))
    print(len(d1))
    # 3.
    # # 1,2,2,3,3,4,4,5,5,n-1,n-1, n-1
    # step= [1]
    # for n in range(N):
    #     step.extend([n,n])
    # step.append(N-1)
    mv = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y = 0, 0
    step = 4
    d2 = [[0 for _ in range(N)] for _ in range(N)]
    visit = d2.copy()
    d1.reverse()
    print(d1)
    for d1_n in d1:
        d2[x][y] = d1_n
        visit[x][y] = 1
        if not(0 <= x+mv[step%4][0] < N and 0 <= y+mv[step%4][1] < N and visit[x+mv[step%4][0]][x+mv[step%4][1]] == 0):
            step += 1

        x += mv[step % 4][0]
        y += mv[step % 4][1]
        print(x,y)

    for v in d2:
        print(v)

    return d2



def continous_explode(mat):
    # 같은 구슬 4개 이상 연속 되면 -1
    # num_mat 1 index 부터 시작해서
    # 연속 cnt +1 -> 4 되면
    # 해당 index 부터 그 앞 count 까지 -1
    do_del = False
    p_ind =[]
    biz = mat[shark][shark-1]
    cnt = 0
    del_i = []
    for i in range(1, number+1):
        for ri, row in enumerate(num_mat):
            if n in row:
                r, c = ri, row.index(n)
        if biz == mat[r][c]:
            cnt += 1
            del_i.append((r,c))
        else:
            p_ind.extend(del_i)
            if cnt >= 4:
                for (dr, dc) in del_i:
                    mat[dr][dc] = 0
                    answer[mat[dr][dc]] += 1
                do_del = True
                del_i = []
                cnt = 1

        biz = mat[r][c]
        return do_del, p_ind

# 마법 시전
for a in num_mat:
    print(a)

for _ in range(M):
    d,s = map(int, input().split())
    p_ind = blizard_explode(shark, d, s) # 1. 폭발

    for ass in mat:
        print(ass)

    move2(p_ind) # 2. 구슬 이동

    print('dddd')
    # 더이상 연속되는거 없을 까지 3,4 반복
    while True:
        do_del, p_ind = continous_explode(mat) # 3. 연속 삭제
        if do_del == False:
            break
        # 4. 구슬 이동
        move2(p_ind)

print(sum(answer))