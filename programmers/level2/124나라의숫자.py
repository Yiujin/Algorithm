from itertools import product

def solution(n): # 효율성 실패 
    num = [1,2,4]

    if n ==1 :
        return "1"
    elif n == 2:
        return "2"
    elif n ==3:
        return "4"
    else:        
        i = 9
        li =[0,3]
        while 1:
            if li[-1] > 500000000:
                break

            li.append(li[-1] + i)
            i = i * 3
        
        # print(len(li), li)

        chk = False
        repeat , idx = 0,0
        for i in range(len(li)):
            if li[i] < n <= li[i+1]:
                chk = True
                repeat = i+1
                idx = i
                break
        
        answer = list(product(num, repeat= repeat))
        answer = answer[n-li[idx]-1]
        # print(answer)
        answer = ''.join(str(x) for x in answer)

        return answer

if __name__ == "__main__":
    # n <= 500,000,000
    n = 1 # 1
    n = 2 # 2
    n = 3 # 4
    n = 4 # 11

    print(solution(9))