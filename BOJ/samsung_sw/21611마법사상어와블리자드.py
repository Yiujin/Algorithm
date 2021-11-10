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
    global answer, mat

    p_ind = []
    rng = magic_direct[d] * s # ex) 3,0
    for i in range(1, s+1):
        drdc = [magic_direct[d][0] * i, magic_direct[d][1] * i]
        # print(drdc)
        # print(shark+drdc[0], shark+drdc[1])
        mat[shark+drdc[0]][shark+drdc[1]] = 0
        # answer[mat[shark+drdc[0]][shark+drdc[1]]+1] += 1 # 폭발한 구슬 개수 세기
        p_ind.append((shark+drdc[0], shark+drdc[1]))
    return p_ind

def move2(p_ind):
    # 1. 1차원으로 만들고
    # 2. 구슬 앞으로 이동
    # 3. 다시 2차원으로 만들기 -> 어차피 그 다음이 연속된거 삭제니까 1차원으로 다시 안만들어도 됨
    drdc = [[1,0], [0,1], [-1,0], [0,-1]] # 아 오 위 왼
    d1 = []
    # 1.
    for n in range(1, number):
        for ri, row in enumerate(num_mat):
            if n in row:
                r, c = ri, row.index(n)
        if mat[r][c] != 0: # 2.
            d1.append(mat[r][c])

    d1.extend([0]* (number-len(d1))) # 안쪽 부터 바깥쪽까지 + 바깥쪽 0으로 채움
    # print(len(d1))
    # d1.reverse() # 2차원으로 만들때 바깥쪽부터 채우니까 뒤집어
    # print(d1)

    return d1

def to2d(d1):
    # 3. 1차원 행렬을 2차원으로
    # # 1,2,2,3,3,4,4,5,5,n-1,n-1, n-1
    # step= [1]
    # for n in range(N):
    #     step.extend([n,n])
    # step.append(N-1)
    mv = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우, 하, 좌, 상
    x, y = 0, 0
    step = 4
    d2 = [[0 for _ in range(N)] for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    d1.reverse()
    # print(d1)
    for d1_n in d1:
        d2[x][y] = d1_n
        visit[x][y] = 1
        # print(f'now : {x},{y} | next : {x+mv[step%4][0]}, {y+mv[step%4][1]}')
        if not(0 <= x+mv[step%4][0] < N and 0 <= y+mv[step%4][1] < N and visit[x+mv[step%4][0]][y+mv[step%4][1]] == 0):
            # print('step change')
            step += 1

        x += mv[step % 4][0]
        y += mv[step % 4][1]
        # print(x,y)

    # print('d2 after blizard')
    # for v in d2:
    #     print(v)

    return d2

def continous_explode(d1):
    global answer

    lend1 = len(d1)
    do_del = False
    # print(d1)
    prev = d1[0]
    cnt = 1
    for i in range(1, lend1):
        if prev == d1[i]:
            cnt += 1
        else:
            if cnt >= 4:
                # print(d1)
                # print(f'biz : {d1[i - 1]}, cnt : {cnt}, i: {i}')
                answer[d1[i - 1]] += cnt
                for j in range(i-cnt, i):
                    d1[j] = 0
                # print(f'after del: \n{d1}, answer : \n{answer}')
                cnt = 1
                do_del = True
            else:
                cnt = 1
        prev = d1[i]

    # print(d1, answer)

    new = []
    for d in d1:
        if d != 0:
            new.append(d)

    new.extend([0] * (number - len(new)))

    return new, do_del

def after_blizard_2d(d1):
    # 1. 구슬 갯수, 구슬 번호 순서대로 만들기
    # 2. 다시 2차원으로 만듬 -> 길이 N*N -1 넘어가면 삭제

    # 1.
    new = []
    prev = d1[0]
    lend1 = len(d1)
    cnt = 1
    for i in range(1, lend1):
        if prev == d1[i]:
            cnt +=1
        else:
            new.append(cnt)
            new.append(d1[i-1])
            cnt = 1
        prev = d1[i]
    # 마지막
    new.append(cnt)
    new.append(d1[-1])
    # print(new)

    # 2.
    # print(number, len(new))
    # print(new)
    if len(new) > number:
        new = new[:number]
        # print('del\n', new)
    else:
        new.extend([0] * (number - len(new)))
    #     print('extend\n', new)
    # print(len(new))
    d2 = to2d(new)

    return d2


# 마법 시전
for _ in range(M):
    d,s = map(int, input().split())
    p_ind = blizard_explode(shark, d, s) # 1. 폭발

    # print('magic')
    # for c in mat:
    #     print(c)

    d1 = move2(p_ind) # 2. 구슬 이동

    # 더이상 연속되는거 없을 까지 3,4 반복
    while True:
        d1, do_del = continous_explode(d1) # 3. 연속 삭제
        if do_del == False:
            break
    # print('after continuous explode: ', d1)
    mat = after_blizard_2d(d1)
    print(mat)

# print(answer)
print(1*answer[1] + 2 * answer[2] + 3*answer[3])