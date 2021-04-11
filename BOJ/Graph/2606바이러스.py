import sys
from collections import deque
def bfs(graph, now, visit):
    cnt = 0
    q = deque([now])

    while q:
        v = q.popleft()
        visit[v] = True
        for i in graph[v]:
            if not visit[i]:
                cnt +=1
                q.append(i)
                visit[i] = True
    print(cnt)



if __name__ == '__main__':
    input = sys.stdin.readline

    n,m = int(input()), int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        i , j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    # print(graph)
    visit = [False] * (n+1)

    bfs(graph, 1, visit)




