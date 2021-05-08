import sys
from collections import deque

def bfs(graph, x,y, row, col):
    q = deque()
    q.append([x, y])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx > row-1 or ty < 0 or ty > col-1 or graph[tx][ty] == 0:
                continue
            else:
                q.append([tx ,ty])
                graph[tx][ty] = 0 # visit
                



if __name__ == "__main__":
    input = sys.stdin.readline
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0 ]

    tc = int(input())

    for _ in range(tc):
        answer = 0
        col, row, n = map(int, input().split()) # 가로길이, 세로길이, 지렁이 갯수
        # print(col, row, n)
        graph = [[0 for _ in range(col)] for _ in range(row)]
        for _ in range(n):
            i, j = map(int, input().split())
            graph[j][i] = 1
        # print(graph)

        for i in range(row):
            for j in range(col):
                if graph[i][j] == 1:
                    bfs(graph, i, j, row, col)
                    answer += 1
        print(answer)
        del graph