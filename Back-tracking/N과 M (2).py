from itertools import combinations

N, M = map(int, input().split())

nums = list(i for i in range(1, N+1))
for num in list(combinations(nums, M)):
    print(*num, sep=' ')