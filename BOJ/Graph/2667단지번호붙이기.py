import sys
from collections import deque
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
def bfs(graph, x ,y):
    apt = 0
    q = deque()
    q.append([x ,y])
    graph[x][y] = 0
    while q:
        row, col = q.popleft()
        apt +=1
        for i in range(4):
            rr = row + dx[i]
            cc = col + dy[i]
            if rr < 0  or rr > n-1 or cc < 0 or cc > n-1 or graph[rr][cc] == 0:
                continue
            else:
                graph[rr][cc] = 0
                # print(graph)
                q.append([rr,cc])
                # print(q)
    # print(apt)
    return apt

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().rstrip())))
    # print(graph)
    
    danji = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                # print(i , j)
                danji.append(bfs(graph, i,j))


    # print(danji)
    danji.sort()

    print(len(danji))
    for x in danji:
        print(x)
    