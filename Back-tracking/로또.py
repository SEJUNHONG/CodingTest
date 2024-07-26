from itertools import combinations

nums = []
while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0 and len(nums) == 1:
        break
    for lotto in combinations(nums[1:], 6):
        print(*lotto)

    print()