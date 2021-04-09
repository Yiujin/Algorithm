def dfs(start, tickets, visit, li):
    global result
    # print(f'visit : {visit}')
    if False not in visit:
        return result.append(li.split(" "))
    else:
        for i in range(len(tickets)):
            if visit[i] == False and tickets[i][0] == start:
                tmp_v = []
                for j in range(len(visit)):
                    tmp_v.append(visit[j])
                tmp_v[i] = True
                dfs(tickets[i][1], tickets, tmp_v, li + " " + tickets[i][1])


def solution(tickets):
    visit = [False] * len(tickets)
    start = "ICN"

    tickets.sort()
    # print(tickets)

    dfs(start, tickets, visit, start)
    return result[0]


if __name__ == '__main__':
    
    test = [
        [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],
        [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]],
        [["ICN", "AAA"], ["AAA", "BBB"], ["AAA", "CCC"], ["CCC", "AAA"], ["BBB", "DDD"]]

    ] 
#     	["ICN", "JFK", "HND", "IAD"]
# 	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
#  ["ICN", "B", "ICN", "A"]
#   ["ICN", "AAA", "CCC", "AAA", "BBB", "DDD"]

    for t in test:
        result =[]
        print(solution(t))