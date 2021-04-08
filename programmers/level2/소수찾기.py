'''
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''
import math
from itertools import permutations
# 제곱근까지만 보고 소수를 판별하는 함수
def is_prime(x):
    if x <= 1 : return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수 아님
    return True


def solution(numbers):
    answer = 0
    l = len(numbers)
    numbers = [x for x in numbers]

    comb =[]
    for i in range(1, l+1):
        comb += list(permutations(numbers, i))
    # print(comb)
    tmp = []
    for i in comb:
        tmp.append(int(''.join(i)))
    
    tmp = list(set(tmp))
    # print(tmp)
    for i in tmp :
        if is_prime(i)==True:
            answer += 1

    return answer

#---------------------------------
# 시간 오래걸림 통과는 함
def solution1(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    try:
        for i in range(2, int(max(a) ** 0.5) + 1):
            a -= set(range(i * 2, max(a) + 1, i))
        return len(a)
    except ValueError:
        return 0

if __name__ == '__main__':
    n = ["17", "011", '000', '020']  # 3, 2, 0, 1
    for i in n:
        print(solution1(i))