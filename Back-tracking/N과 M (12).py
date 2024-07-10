from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
answer = []
for num in list(combinations_with_replacement(nums, M)):
    answer.append(num)

answer = sorted(list(set(answer)))

for numbers in answer:
    print(*numbers, sep=' ')