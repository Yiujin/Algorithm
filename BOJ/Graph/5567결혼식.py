import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
# print(g)
v = [0 for _ in range(n+1)]
# print(v)
q = deque()
q.append(1) 
v[1] = 1
while q:
    fr = q.popleft()
    for i in g[fr]:
        if v[i] == 0:
            q.append(i)
            v[i] = v[fr]+1
try:
    print(v.index(3) - 1)
except:
    print(0)