from collections import deque

def bfs():
    q = deque()
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]

    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if tomatos[h][i][j] == 1:
                    q.append((h, i, j))
                    visited[h][i][j] = 1
                elif tomatos[h][i][j] == 0:
                    cnt += 1
    while q:
        z, x, y = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and visited[nz][nx][ny] == 0 and tomatos[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                visited[nz][nx][ny] = visited[z][x][y] + 1
                cnt -= 1
    if cnt == 0:
        return visited[z][x][y] - 1
    else:
        return -1

M, N, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
print(bfs())

