from collections import deque

N = int(input())
jido = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
danji = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global danji, visited
    q = deque()
    q.append((x, y))

    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and jido[nx][ny] != 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    danji.append(cnt)




for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and jido[i][j] != 0:
            bfs(i, j)

danji.sort()
print(len(danji))
for d in danji:
    print(d)