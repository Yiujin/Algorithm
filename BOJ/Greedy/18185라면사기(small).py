if __name__ == "__main__": # 틀림 다시풀기
    n = int(input())

    l = list(map(int, input().split()))
    total = 0
    # 공장 3개에서 하나 씩 사는 경우
    for i in range(0, n-2):
        buy = min(l[i], l[i+1], l[i+2])
        l[i] -= buy
        l[i+1] -= buy
        l[i+2] -= buy
        total += buy * 7
   
    # 공장 2개에서 하나씩 사는 경우
    for i in range(0, n-1):
        buy = min(l[i], l[i+1])
        l[i] -= buy
        l[i+1] -= buy
        total += buy * 5

    # 공장 하나에서 사는 경우
    ll = [x for x in l if x > 0] * 3
    total += sum(ll)

    print(total)
    
