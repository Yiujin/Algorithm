import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    row, col = map(int, input().split())

    graph = []
    for i in range(row):
        graph.append(list(map(int, input().rstrip())))
    # print(graph)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append([0,0])

    while q:
        x , y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < row and 0 <= ty < col and graph[tx][ty] == 1:
                q.append([tx, ty])
                graph[tx][ty] = graph[x][y] + 1

    # print('result: ' , graph)
    print(graph[row-1][col-1])



