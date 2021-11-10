'''
https://www.acmicpc.net/problem/20057

A[r][c]는 (r, c)에 있는 모래의 양

1. 가운데 칸부터 한칸씩 밖으로 이동

x->y 이동 시
2. y의 모든 모래 주변으로 이돈
3. x가 y있는 곳으로 이동

토네이도 중간부터 0,0 까지 이동 후 소멸
격자 밖으로 나간 모래의 양?

3 ≤ N ≤ 499
N은 홀수
0 ≤ A[r][c] ≤ 1,000
가운데 칸에 있는 모래의 양은 0
'''

# main
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

# 번호 행렬 만들기
number = n*n-1
num_mat = [[0]*n for _ in range(n)]
drdc=[(0,1), (1,0), (0,-1), (-1,0)] # 우하좌상
step = 0;
r,c = 0,0
for num in range(number, 0, -1):
    num_mat[r][c] = num
    if not(0<=r+drdc[step%4][0]<n and 0<=c+drdc[step%4][1]<n and num_mat[r+drdc[step%4][0]][c+drdc[step%4][1]] == 0):
        step += 1

    r += drdc[step%4][0]
    c += drdc[step%4][1]

for m in num_mat:
    print(m)


