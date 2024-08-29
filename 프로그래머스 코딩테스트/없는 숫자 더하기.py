def solution(numbers):
    nums = [i for i in range(10)]
    return sum(set(nums) - set(numbers))