import sys
from bisect import bisect_left, bisect_right

if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input())
    card = sorted(list(map(int, input().split())))
    M = int(input())
    M_list = list(map(int, input().split()))

    for m in M_list:
        lower_bound = bisect_left(card, m)
        upper_bound = bisect_right(card, m)
        print(upper_bound-lower_bound)


# from sys import stdin

# N = int(input())
# arr_n = list(map(int,stdin.readline().split()))
# M = int(input())
# arr_m = list(map(int,stdin.readline().split()))

# dic = dict()

# for i in arr_n:
#     try :
#         dic[i] += 1
#     except:
#         dic[i] = 1

# for i in arr_m:
#     try:
#         print(dic[i])
#     except:
#         print('0')