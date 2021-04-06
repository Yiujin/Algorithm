def solution(s):
    if len(s) == 1:
        return 1
    half = (len(s)//2)+1
    str_len =  list(range(1,half))
    min_len = 1000
    for sl in str_len:
        sub = [s[i:i+sl] for i in range(0,len(s),sl)]
        # print(sub)

        ll = len(sub)
        tmp=1
        answer = ''
        for i in range(0,ll-1):
            if sub[i] == sub[i+1]:
                tmp += 1
            else:
                if tmp == 1:
                    answer += f'{sub[i]}'
                else:
                    answer += f'{tmp}' + f'{sub[i]}'
                tmp = 1
        if tmp == 1:
            answer += f'{sub[i+1]}'
        else:
            answer += f'{tmp}' + f'{sub[i+1]}'           
        # print(answer)

        tt = len(answer)
        # print(tt, min_len)
        if tt < min_len:
            min_len = tt

    return min_len

if __name__ == '__main__':
    st = ["aabbaccc",	#7 1개
        "ababcdcdababcdcd", #9	8개
        "abcabcdede", #8 3개
        "abcabcabcabcdededededede",	#14 6개
        "xababcdcdababcdcd", #17 no cutting
        "a"] #1

    for s in st:
        print(solution(s)) 

