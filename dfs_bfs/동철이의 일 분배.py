T = int(input())

def dfs(n, sm):
    global answer
    if answer >= sm:
        return
    if n == N:
        answer = max(answer, sm)
        return
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, sm*(case[n][j]/100))
            visited[j] = 0

for x in range(1, T+1):
    answer = 0
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    dfs(0, 100)
    print(f'#{x} {answer:.6f}')