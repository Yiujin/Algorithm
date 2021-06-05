import sys

def binary_search(start, end, A, target):
    while start <= end:
        mid = (start+end) // 2
        # print('mid: ', mid)
        if A[mid] == target:
            return mid
        if A[mid] > target:
            end = mid - 1
        if A[mid] < target:
            start = mid + 1
    return None 

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    A = sorted(list(map(int, input().split())))
    M = int(input())
    m = list(map(int, input().split()))

    start = 0
    end = len(A)-1
    # print('start. end : ', start, end)

    for mm in m:
        # print("mm", mm)
        if binary_search(start, end, A, mm) is not None:
            print('1')
        else:
            print('0')
            
        
    