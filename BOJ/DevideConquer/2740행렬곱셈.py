# import sys

# if __name__ == '__main__':
#     input = sys.stdin.readline

#     row1, col1 = map(int, input().split())
#     mat1 = [list(map(int, input().split())) for i in range(row1)]
#     row2, col2 = map(int, input().split())
#     mat2 = [list(map(int, input().split())) for i in range(row2)]
#     mat2 = [x for x in zip(*mat2)]
#     # print(mat1, mat2)
#     for m1 in mat1:
#         for m2 in mat2:
#             print(m1[0]*m2[0] + m1[1]*m2[1], end = ' ')
#         print()

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    row1, col1 = map(int, input().split())
    mat1 = [list(map(int, input().split())) for i in range(row1)]
    row2, col2 = map(int, input().split())
    mat2 = [list(map(int, input().split())) for i in range(row2)]
    result = [[0 for _ in range(col2)] for _ in range(row1)]
    # print(result)
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += mat1[i][k]*mat2[k][j]

    for i in range(row1):
        for j in range(col2):
            print(result[i][j], end = ' ')
        print()