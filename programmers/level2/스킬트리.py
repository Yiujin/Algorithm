def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        idx = []
        chk = False
        for j in skill:
            if j in i:
                idx.append(i.index(j))
            else:
                idx.append(100)
        # print(idx)
        for i in range(len(idx)-1):
            if idx[i] > idx[i+1]:
                chk = True
        if chk == False:
            answer +=1

    return answer

if __name__ == "__main__":
    skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"] #2
    skill1, skill_trees = "AC", ["BACDE", "CBADF", "AECB", "BDA"] #3


    print(solution(skill1, skill_trees))