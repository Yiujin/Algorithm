import sys
import heapq
INF = int(10e9)

def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start)) # 비용, 노드

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 최단거리로 방문했으면 넘어감
            continue
        for i in graph[now]: # 인접 노드
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

if __name__ == "__main__":
    input = sys.stdin.readline

    v, e = map(int, input().split())
    start = int(input())

    distance = [INF] * (v+1)
    graph = [[] for i in range(v+1)]
    for _ in range(e):
        a,b,c = map(int, input().split())
        graph[a].append((c, b)) # a->b 비용 = c
    # print(graph)
    for con in graph:
        con.sort()
    # print(graph)
    distance[start] = 0
    dijkstra(graph, distance, start)
    # print(distance)
    for c in distance[1:]:
        if c == INF:
            print("INF")
        else:
            print(c)
