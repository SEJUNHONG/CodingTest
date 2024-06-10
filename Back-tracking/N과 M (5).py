from itertools import permutations
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for num in permutations(nums, M):
    num = list(num)
    print(*num, sep=' ')