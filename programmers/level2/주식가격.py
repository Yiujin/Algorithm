from collections import deque

def sol2(prices):
    answer = [0] * len(prices)
    q = deque(prices)
    j = 0
    while q:
        front = q.popleft()
        # 효율성 통과 x        
        # for i in range(len(q)):
        #     answer[j] += 1
        #     if front > q[i]:
        #         break

        # 효율성 통과 o
        for i in q:
            answer[j] += 1
            if front > i:
                break
        j += 1

    # print(answer)
    return answer

# 정확성, 효율성 모두 통과
def solution(prices):
    answer = [0] * len(prices)
    k = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[k] += 1
            else:
                answer[k] += 1
                break
        k +=1 

    return answer

if __name__ == "__main__":
    price = [1,2,3,2,3] #[4,3,1,1,0]
    price2 = [5,4,3,2,1] #[1,1,1,1,0]
    price3 = [3,2,3,3,1] #[1,3,2,1,0]
    price4 = [5,5,4,3,4,5] #[2,1,1,2,1,0]

    # solution(price)
    # solution(price2)
    # solution(price3)
    # solution(price4)
    sol2(price)
    sol2(price2)
    sol2(price3)
    sol2(price4)


