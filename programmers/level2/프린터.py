def solution(priorities, location): # 다시풀기
    cnt = 0
    q = [(i, d) for i, d in enumerate(priorities)]
    print(q)

    while True:
        front = q.pop(0)
        if any(front[1] < i[1] for i in q):
            q.append(front)
        else:
            cnt += 1
            if front[0] == location:
                print(cnt)
                return cnt
    

if __name__ == "__main__":
    priorities, location = [2,1,3,2], 2 #1
    priorities2, location2 = [1,1,9,1,1,1], 0 #5 
    priorities3, location3 = [2,1,3,2,4,1], 2 #2  / 4,1,2,1,3*,2 -> 3*,2,1,2,1 -> 2,1,1 ->...
    priorities4, location4 = [1,1,2,3,1,1], 0 #5  / 3,1,1,1*,1,2 -> 2,1,1,1*,1 -> 1,1,1*,1 -> ... 
    priorities5, location5 = [2,1,2,2,4,1], 2 #3  / 4,1,2,1,2*,2 -> 2,1,2*,2,1 -> 2*,2,1,1 -> ...
    priorities6, location6 = [8,5,8,4,6,5,7,4], 4 #4  / 8,5,8,4,6*,5,7,4 -> 8,4,6*,5,7,4,5 -> 7,4,5,4,6*,5 -> 6*,5,4,5,4 
    priorities7, location7 = [2,1,2,1,2], 2 #2  
    priorities8, location8 = [2,1,2,1,2], 1 #4 / 2,1*,2,1,2 -> 2,1,2,1* -> 2,1*,1 -> 1*,1 
    location9, location10 = 3,4  # 4, 3

    solution(priorities, location)
    solution(priorities2, location2)
    solution(priorities3, location3)
    solution(priorities4, location4)
    solution(priorities5, location5)
    solution(priorities6, location6)
    solution(priorities7, location7)
    solution(priorities7, location8)
    # solution(priorities7, location9)
    # solution(priorities7, location10)








