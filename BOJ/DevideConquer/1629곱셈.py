import sys
from typing import Dict
input = sys.stdin.readline

A, B ,C = map(int, input().split())
# B 짝수일 경우 : (A^(B//2) ^2) % C
# B 홀수일 경우 : (A^(B//2) ^2)*A % C
def power(A,B):
    if B ==1:
        return A%C
    else:
        basic = power(A,B//2)
        if B % 2 ==0: 
            return int(basic*basic % C)
        else:
            return int(basic*basic*A % C)

print(power(A,B))
