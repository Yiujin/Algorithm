import sys
from bisect import bisect_left

if __name__ == '__main__':
    input = sys.stdin.readline

    N, C = map(int, input().split())
    house = []
    for i in range(N):
        house.append(int(input()))
    house.sort()
    # print(house)

    min_ = 1 # 최소 간격
    max_ = max(house) - min(house) # 최대 간격
    
    length = len(house)-1
    # 매개변수 : mid - 공유기 설치하는 거리 / -> 공유기 갯수 달라짐
    while 1:
        mid = (max_+min_) // 2
        num_c = 0
        start_idx = 0
        # print(f'mid: {mid}')
        while start_idx <= length:
            num_c +=1
            start_idx = bisect_left(house, house[start_idx]+mid)
        if num_c >= C: # 설치한 공유기 갯수가 필요한 공유기 갯수보다 많으면 mid 증가
            min_ = mid + 1
        elif num_c < C: # 설치한 공유기 갯수가 필요한 공유기 갯수보다 적으면 mid 감소
            max_ = mid -1
        if mid == max_:
            print(mid)
            break
