from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
INF = 1e9

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[INF]*N for _ in range(N)]
    visited[x][y] = jido[x][y]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] > visited[x][y] + jido[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + jido[nx][ny]
    return visited[N-1][N-1]

T = int(input())
for C in range(1, T+1):
    N = int(input())
    jido = [list(map(int, input())) for _ in range(N)]

    print(f'#{C} {bfs(0, 0)}')