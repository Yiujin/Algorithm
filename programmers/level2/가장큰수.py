def check(a,piv):
    if int(a+piv) > int(piv+a):
        return True
    else:
        return False


def quick(numbers):
    '''
    quick sort
    1<len(numbers)<100,000
    1 <= 원소값 <= 1000
    '''
    if len(numbers) <= 1:
        return numbers

    numbers = list(map(str, numbers))

    pivot = numbers[0]
    tail = numbers[1:]
    
    left = [x for x in tail if check(x,pivot) == True]
    right = [x for x in tail if check(x,pivot) == False]
    # print(left, right)

    return quick(left) + [pivot] + quick(right)

def solution(numbers):
    tmp = list(set(numbers))
    if len(tmp) == 1 and tmp[0] == 0:
        return "0"
    
    res = quick(numbers)
    return ''.join(res)

#-----------------------
from functools import cmp_to_key

def comp(a,b):
    ab = a+b
    ba = b+a
    return (ab > ba) - (ab < ba) # ab>ba : 1 / ab < ba : -1 / ab == ba : 0 return

def solution1(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = cmp_to_key(comp), reverse = True)

    print(numbers)
    return str(int(''.join(numbers)))
    
if __name__ == "__main__":
    numbers = [[0,0,0,0], #"0"
            [1000,1], #"11000"
            [6, 10, 2], #"6210" 
            [3, 30, 34, 5, 9],#"9534330"
            [21,27,24,29,20], #"2927242120"
            [2,22,222,2222]]   #"2222222222"

    for n in numbers:
        print(solution1(n))