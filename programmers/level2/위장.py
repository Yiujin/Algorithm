from collections import Counter
from functools import reduce
def solution(clothes):
    #Counter = 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체
    #dict반환
    cnt = Counter([kind for name, kind in clothes])
    # print(cnt)
    
    # reduce 다 곱해서 하나의 값으로 반환
    # 공식 = 경우의 수 / 입거나 안입거나 = 옷개수 + 1 
    answer = reduce(lambda x, y: x*y, [a+1 for a in cnt.values()]) - 1
    return answer