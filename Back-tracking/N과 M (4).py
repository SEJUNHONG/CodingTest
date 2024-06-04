from itertools import combinations_with_replacement

N, M = map(int, input().split())

nums = list(i for i in range(1, N+1))
for num in list(combinations_with_replacement(nums, M)):
    print(*num, sep=' ')