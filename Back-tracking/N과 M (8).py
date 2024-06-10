from itertools import combinations_with_replacement
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for num in combinations_with_replacement(nums, M):
    num = list(num)
    print(*num, sep=' ')