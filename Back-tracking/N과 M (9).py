from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
answer = []
for num in list(permutations(nums, M)):
    answer.append(num)

answer = sorted(list(set(answer)))

for numbers in answer:
    print(*numbers, sep=' ')