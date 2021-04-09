from collections import deque

def adj(a,b):
    cnt=0
    for i,j in zip(a,b):
        if i != j:
            cnt+=1
    if cnt == 1:
        return True
    return False

def bfs(words, now, visit):
    q = deque()
    q.append(now)
    
    while q:
        v = q.popleft()
        for w in words:
            if adj(v, w) and w not in visit:
                q.append(w)
                visit[w] = visit[v] + 1
                # print(visit)
            

def solution(begin, target, words):
    visit = {begin : 0}
    
    if target not in words:
        return 0
    else:
        bfs(words, begin, visit)
        return visit[target]
    
if __name__ == '__main__':
    tc = [
        ["hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]],
        ["hit",	"cog",	["hot", "dot", "dog", "lot", "log"]],
        ["hit","hot",["hot", "dot", "dog", "lot", "log"]]
    ]

    for t in tc:
        print(solution(t[0], t[1] , t[2]))
    