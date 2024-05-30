from itertools import permutations

N, M = map(int, input().split())

nums = list(i for i in range(1, N+1))
for num in list(permutations(nums, M)):
    print(*num, sep=' ')