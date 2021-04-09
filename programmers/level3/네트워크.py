# def dfs(start, visited, computers):
    
#     visited[start] = True
#     n = len(computers)
#     # print(f'{start} ��° ��� | visited : {visited}')
#     for j in range(0, n):
#         # print(f"�������� computers[{start}][{j}] : {computers[start][j]}")
#         if computers[start][j] == 1 and visited[j] == False:
#             dfs(j, visited, computers)
        

# def solution(n, computers):
#     answer = 0
#     visited = [False] * n
    
#     for i in range(n):
#         if visited[i] == False:
#             dfs(i, visited, computers)
#             answer += 1
    
#     return answer

from collections import deque
def bfs(graph, now,  visit, n):
    if visit[now]:
        return False
    q = deque([now])
    visit[now] = True
    while q:
        v= q.popleft()
        for i in range(n):
            if graph[v][i] == 1 and not visit[i]:
                q.append(i)
                visit[i] = True

    print(f'visit : {visit}')
    return True
            

def solution(n, computers):
    cnt = 0
    visit = [False for _ in range(n)]
    for i in range(n):
        print(f"i : {i} 번 computer")
        if bfs(computers, i, visit, n):
            cnt += 1
    print(cnt)    
    return cnt

if __name__ == '__main__' :
    n0 , com0 = 3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	#2
    n1, com1 = 3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	#1
    n2, com2 = 1, [[1]]

    solution(n0, com0)
    solution(n1, com1)
    solution(n2, com2)
