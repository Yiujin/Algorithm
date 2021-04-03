def gcd(x ,y): # 다시 풀기 
    while y:
        x, y = y, x%y
    return x

def solution(w,h):
    return w * h - (w + h - gcd(w,h)

if __name__ == "__main__":
    w, h = 8, 12 # 80
    w1, h1 = 3 , 4 # 6
    print(solution(w,h))
    print(solution(w1,h1))
    