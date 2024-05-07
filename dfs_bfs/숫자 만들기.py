T = int(input())

def dfs(n, num, plus, minus, mul, div):
    global max_num, min_num
    if n == N:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    if plus:
        dfs(n+1, num+nums[n], plus-1, minus, mul, div)
    if minus:
        dfs(n+1, num-nums[n], plus, minus-1, mul, div)
    if mul:
        dfs(n+1, num*nums[n], plus, minus, mul-1, div)
    if div:
        dfs(n+1, int(num/nums[n]), plus, minus, mul, div-1)

for t in range(1, T+1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    nums = list(map(int, input().split()))
    max_num, min_num = -1e9, 1e9
    dfs(1, nums[0], plus, minus, mul, div)

    print(f'#{t} {max_num - min_num}')