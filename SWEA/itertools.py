# 조합 : n개 중에서 중복없이 r개를 뽑음, 이때 순서 상관없음(순서가 다르고 원소가 같으면 같은 걸로 침)
def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            return [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next

# 중복조합 : n개 중에서 중복 포함하여 r개를 뽑음, 이때 순서 상관없음
def combinations_with_replacement(arr, r):
    for i in range(len(arr)):
        if r == 1:
            return [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:], r-1):
                yield [arr[i]] + next

# 순열 : n개 중에서 중복없이 r개를 뽑음, 이때 순서 상관있음(순서가 다르고 원소가 같으면 다른 걸로 침)
def permutations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            return [arr[i]]
        else:
            for next in permutations(arr[:i] + arr[i+1:], r-1):
                yield [arr[i]] + next


# 중복 순열 : n개 중에서 중복 포함하여 r개를 뽑음, 이때 순서 상관있음
def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            return [arr[i]]
        else:
            for next in product(arr, r-1):
                yield [arr[i]] + next