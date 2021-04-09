from itertools import product

def solution(numbers, target):
    l = [(i, -i) for i in numbers]

    p = product(*l)
    # print(p)
    count = 0
    s =  list(map(sum, p))
    print(s)
    # print(s.count(target))
    return s.count(target)
if __name__ == '__main__':
    n , t = [1, 1, 1, 1, 1], 3
    solution(n,t)