from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * M for _ in range(N)]

    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return visited[N-1][M-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and miro[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(bfs(0, 0))