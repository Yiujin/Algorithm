import sys
input = sys.stdin.readline
import heapq # 우선순위큐를 이용하여 빠르게 중앙 값 찾기

n = int(input())
maxheap, minheap = [], [] # maxheap의 모든 원소는 minheap의 모든 원소보다 작아야함
for i in range(n):
    if len(maxheap) == len(minheap):
        heapq.heappush(maxheap, -int(input()))
    else:
        heapq.heappush(minheap, int(input()))
    
    if not minheap:
        print(-maxheap[0])
        continue

    if -maxheap[0] > minheap[0]: 
        # maxheap에서 제일 큰 원소가 minheap의 제일 작은 원소보다 크다면 
        # 두 원소를 바꾸어 넣기
        max_tmp = -heapq.heappop(maxheap)
        min_tmp = heapq.heappop(minheap)
        heapq.heappush(minheap, max_tmp)
        heapq.heappush(maxheap, -min_tmp)
    print(-maxheap[0])



    

