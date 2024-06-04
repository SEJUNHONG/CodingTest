from itertools import product

N, M = map(int, input().split())

nums = list(i for i in range(1, N+1))
for num in list(product(nums, repeat=M)):
    print(*num, sep=' ')