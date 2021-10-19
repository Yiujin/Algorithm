# 길이 N 컨베이어 벨트 / 2N 벨트
'''
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다. / 로봇이 내리는 위치에 도달하면(Nd으로 가는 순간) 내려야됨
2. 가장 먼저 벨트에 올라간 로봇->젤 뒤인덱스 에 있는 애
부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3.올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4.내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

몇 번째 단계가 진행 중일때 종료되었는지 출력한다.

2 ≤ N ≤ 100
1 ≤ K ≤ 2N  K : 내구도가 0인 칸의 갯수 threshold
1 ≤ Ai ≤ 1,000 : Ai = 각 칸의 내구도
'''

def rotate(A):
    new =[A[-1]]
    new.extend(A[: -1])
    return new

if __name__ == '__main__':
    N,K = map(int, input().split())
    A = list(map(int, input().split())) # 내구도 , 절반 기준 reserve된 상태
    robot = [0 for _ in range(N)]

    ans = 0
    while True:
        # print(robot)
        ans += 1
        # 1. 회전 후 로봇 내려
        A = rotate(A)
        robot = rotate(robot)
        robot[-1] = 0


        # 2. 다음칸에 로봇 없고, 그 칸에 내구도 1이상 이면 로봇 한칸 이동해
        for i in range(N-1, 0, -1):
            if robot[i-1] == 1 and robot[i] == 0 and A[i] >= 1:
                # print('robot move')
                robot[i] = 1 # 로봇 이동
                robot[i-1] = 0
                A[i] -= 1 # 내구도 -1
        robot[-1] = 0
        # print('robot: ', robot)
        # print('A: ' ,A)


        # 3. 올리는 위치 내구도 1 이상이면  로봇 올려
        if A[0] > 0:
            robot[0] = 1
            A[0] -= 1

        # 4. 내구도 0인거 K개 이상이면 끝
        if A.count(0) >= K:
            break

    print(ans)
