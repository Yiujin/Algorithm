import sys
input = sys.stdin.readline
t = int(input())

dptable = {0 : (1,0), 1: (0,1)}
zero, one = 0,0
for i in range(t):
    n = int(input())
    try:
        print(f'{dptable[n][0]} {dptable[n][1]}')
    except:
        # tmp = dptable에 있는 키값 중 제일 큰 값
        tmp = max(list(dptable.keys())) 

        while tmp+1 <= n:
            dptable[tmp+1] = (dptable[tmp][0] + dptable[tmp-1][0], 
                            dptable[tmp][1] + dptable[tmp-1][1])
            tmp+=1
        print(f'{dptable[n][0]} {dptable[n][1]}')