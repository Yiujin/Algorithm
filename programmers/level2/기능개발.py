import math

def solution(progresses, speeds):
    answer = []

    day = []
    for p, s in zip(progresses, speeds):
        day.append(math.ceil((100 - p) / s))
    # print(day)

    if len(set(day)) == 1:
        return [1]

    max_ = day.pop(0)
    ans = 1
    while day:
        tmp = day.pop(0)
        if max_ >= tmp:
            ans += 1
        else :
            answer.append(ans)
            max_ = tmp
            ans = 1
    answer.append(ans)

    return answer

if __name__ == "__main__":
    progresses, speeds = [93, 30, 55], [1,30,5]  # [2,1] 7,3,9
    progresses2, speeds2 = [95, 90, 99, 99, 80, 99], [1,1,1,1,1,1] # [1,3,2] 5,10,1,1,20,1
    progresses3, speeds3 = [96,97,98], [1,1,1] # [3] 4,3,2
    progresses4, speeds4 = [99,99,99], [1,1,1] # [1] 1,1,1
    progresses5, speeds5 =  [40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7] # [1,2,3] / 1,7,3,9,4,5
    progresses6, speeds6 =  [93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7] # [2,4] / 7,3,9,4,1,5




    print(solution(progresses, speeds))
    print(solution(progresses2, speeds2))
    print(solution(progresses3, speeds3))
    print(solution(progresses4, speeds3))
    print(solution(progresses5, speeds5))
    print(solution(progresses6, speeds6))


