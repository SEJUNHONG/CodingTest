T = int(input())

def dfs(n, sm, now):
    global answer

    if answer <= sm:
        return

    if n == N-1:
        answer = min(answer, sm+jido[now][0])
        return

    for j in range(1, N):
        if not visited[j]:
            visited[j] = True
            dfs(n+1, sm+jido[now][j], j)
            visited[j] = False

for test_case in range(1, T+1):
    N = int(input())

    answer = 100 * 100
    visited = [False] * N

    jido = [list(map(int, input().split())) for _ in range(N)]

    dfs(0, 0, 0)
    print(f'#{test_case} {answer}')