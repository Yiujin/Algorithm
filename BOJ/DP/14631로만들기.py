if __name__ == "__main__":
    n = int(input())

    # d[i] = min(d[i/3], d[i/2], d[i-1])+1
    d = [0] * 1000001
    for i in range(2, n+1):
        d[i] = d[i-1] + 1 # 현재의 수에서 1 빼는 경우
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2]+1)
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3]+1)

    print(d[n])
