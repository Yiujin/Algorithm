import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
for i in range(n):
    tmp = int(input())
    if tmp > 0:
        heapq.heappush(heap, (-tmp, tmp))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print('0')
        