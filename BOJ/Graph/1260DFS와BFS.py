from collections import deque

def dfs(graph, v , visit):
    visit[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

def bfs(graph, now, visit):
    q = deque([now])
    visit[now] =True

    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = True


if __name__ == '__main__':
    n,m,v = map(int, input().split())
    visit = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    # print(graph)
    for i in range(m):
        i,j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    for i in graph:
        i.sort()
    # print(graph)

    dfs(graph, v, visit)
    print()
    visit = [False] * (n+1)
    bfs(graph, v, visit)
