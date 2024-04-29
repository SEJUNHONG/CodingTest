T = int(input())

def dfs(n, sm):
    global answer
    if answer <= sm:
        return

    if n == N:
        answer = min(answer, sm)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            dfs(n+1, sm+factory[n][j])
            visited[j] = False


for test_case in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    answer = 100 * N
    visited = [False] * N
    dfs(0, 0)
    print(f'#{test_case} {answer}')
