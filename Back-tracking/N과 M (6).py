from itertools import combinations
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for num in combinations(nums, M):
    num = list(num)
    print(*num, sep=' ')