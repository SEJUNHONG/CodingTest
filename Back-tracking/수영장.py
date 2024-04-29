T = int(input())

def dfs(n, sm):
    global answer
    if answer <= sm:
        return
    if n > 12:
        answer = min(answer, sm)
        return

    dfs(n+1, sm+day*swim[n])
    dfs(n+1, sm+month)
    dfs(n+3, sm+three)
    dfs(n+12, sm+year)

for test_case in range(1, T+1):
    answer = 1e9

    day, month, three, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))

    answer = min(answer, year)
    dfs(1, 0)

    print(f'#{test_case} {answer}')
