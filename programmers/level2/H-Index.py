def solution(citations):
    answer = 0
    start = min(citations)
    end = max(citations)
    chk = True;l = len(citations)
    for x in citations:
        if x < l:
            chk = False
    if chk == True:
        return l

    while start<=end:
        total = 0
        h = (start + end) //2
        for x in citations:
            if x-h >= 0:
                total += 1

        if h <= total:
            answer = h
            start = h +1
        else:
            end = h-1

    return answer


if  __name__ == "__main__":
    cit = [[3, 0, 6, 1, 5], [16,6,6,6,1], [20,21,22,23], [1,1,1], [0,0,0,0]] # 3,4,4,1,0
     

    for c in cit:
        print(solution(c))
    
