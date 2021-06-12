mport sys
input = sys.stdin.readline

# dptable = 지원이가 만들 수 있는 타일의 갯수
# dptable = n:짝수 -> 
dptable = [0, 1 ,2]
n = int(input())
for i in range(3,n+1):
    dptable.append((dptable[i-1] + dptable[i-2])%15746)
print(dptable[n])