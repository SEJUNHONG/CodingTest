T = int(input())

def dfs(n):
    global answer
    if n == N:
        answer = max(answer, int("".join(map(str, nums))))
        return

    for i in range(L-1):
        for j in range(i+1, L):
            nums[i], nums[j] = nums[j], nums[i]

            check = int("".join(map(str, nums)))*10+n
            if check not in visited:
                dfs(n+1)
                visited.append(check)
            nums[i], nums[j] = nums[j], nums[i]

for C in range(1, T+1):
    answer = 0
    num, N = input().split()
    N = int(N)
    nums = []
    for n in num:
        nums.append(int(n))
    L = len(nums)
    visited = []
    dfs(0)
    print(f'#{C} {answer}')