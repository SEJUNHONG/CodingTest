T = int(input())

dx = [1, 1, -1, -1, 1]
dy = [-1, 1, 1, -1, -1]

def dfs(n, start_x, start_y, v):
    global answer
    if n == 2 and answer >= len(v)*2:
        return
    if n > 3:
        return
    if n == 3 and (x, y) == (start_x, start_y):
        answer = max(answer, len(v))
        return

    for i in range(n, n+2):
        nx, ny = start_x + dx[i], start_y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and jido[nx][ny] not in v:
            v.append(jido[nx][ny])
            dfs(i, nx, ny, v)
            v.pop()

for t in range(1, T+1):
    N = int(input())
    jido = [list(map(int, input().split())) for _ in range(N)]
    answer = -1

    for x in range(N-2):
        for y in range(1, N-1):
            dfs(0, x, y, [])
    print(f'#{t} {answer}')