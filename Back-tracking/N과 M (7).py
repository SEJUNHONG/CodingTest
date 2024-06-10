from itertools import product
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for num in product(nums, repeat=M):
    num = list(num)
    print(*num, sep=' ')