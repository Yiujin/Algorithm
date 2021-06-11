import sys
input = sys.stdin.readline
import heapq

n = int(input())
minheap = []
for i in range(n):
    tmp = int(input())
    if tmp >0:
        heapq.heappush(minheap, tmp)
    else:
        if len(minheap) > 0:
            print(heapq.heappop(minheap))
        else: 
            print('0')