def solution(p):
    p = sorted(p) 
    print(p)
    
    for i ,j in zip(p, p[1:]):
        print(i, j)
        if j.startswith(i) or i.startswith(j):
            return False
    return True

if __name__ == '__main__':
    ppp =  [["119", "97674223", "1195524421"],
["123","456","789"],
["12","123","1235","567","88"],
["119", "97674223", "21195524421"], ['12']
]

for  p in ppp :
    print(solution(p))