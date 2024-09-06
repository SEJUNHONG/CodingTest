from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, v):
    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and v[nx][ny] == 0 and ices[nx][ny] > 0:
                q.append((nx, ny))
                v[nx][ny] = 1



N, M = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(N)]

for year in range(1, 900000):
    visited = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if ices[x][y] != 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < M and 0 <= ny < N and ices[nx][ny] == 0:
                         visited[x][y] == 1

    for x in range(N):
        for y in range(M):
            if visited[x][y] > 0:
                ices[x][y] = max(0, ices[x][y] - visited[x][y])

    v = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == 0 and ices[i][j] > 0:
                bfs(i, j, v)
                cnt += 1
                if cnt > 1:
                    answer = year
                    break

    if cnt == 0:
        answer = 0
        break
print(answer)
