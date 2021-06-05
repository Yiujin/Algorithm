import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    K, N = map(int, input().split())
    lan = []
    for _ in range(K):
        lan.append(int(input()))
    lan.sort()

    start = 0
    end = sum(lan) // N
    result = 0

    while start <= end:
        total = 0
        if (start+end) >= 2:
            mid = (start+end) // 2
        else:
            mid = start+end
        # print('mid :', mid)
        for i in lan:
            total += i // mid
        if total >= N:
            result = mid
            start = mid + 1
        else:
            end = mid -1

    print(result)
