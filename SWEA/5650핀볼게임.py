# 블록 : 1,2,3,4,5
# 웜홀 6~10 -> 반드시 쌍으로, 최소 0개 ~ 최대 5쌍
# 블랙홀 -1 -> 0개 ~ 최대 5개

# 핀볼 상하좌우
# 벽이나 블록 부딪히면 진행 방향 바뀜 / 점수  +
# 웜홀에 빠지면 동일한 숫자를 가진 반대편 웜홀로 빠져나옴 / 진행방향 그대로
# 블랙홀 만나면 또는 출발위치로 돌아오면 게임 끝

# 게임판 위에서 출발 위치와 진행 방향을 임의로 선정가능 할 때,
# 게임에서 얻을 수 있는 점수의 최댓값을 구하여라! -< bfs
# 단, 블록, 웜홀 또는 블랙홀이 있는 위치에서는 출발할 수 없다.

def block(mat, N, cur_d, b_num):
    if b_num == 1:
    


def bfs(mat, N):




# main
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        mat = []
        for _ in range(N):
            mat.append(map(int, input.split()))

