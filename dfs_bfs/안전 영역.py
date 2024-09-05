from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, n):
    q = deque()
    q.append((x, y))

    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and towns[nx][ny] > n:
                q.append((nx, ny))
                visited[nx][ny] = 1

N = int(input())
towns = [list(map(int, input().split())) for _ in range(N)]

max_town = 0
for i in range(N):
    max_town = max(max_town, max(towns[i]))

max_cnt = 0
for n in range(max_town):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and towns[i][j] > n:
                bfs(i, j, n)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)