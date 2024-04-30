from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    fishes = []

    q.append((x, y))
    visited[x][y] = 1
    dist = 0

    while q:
        x, y = q.popleft()
        if dist == visited[x][y]:
            return fishes, dist-1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and shark_size >= jido[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if shark_size > jido[nx][ny] > 0:
                    fishes.append((nx, ny))
                    dist = visited[nx][ny]
    return fishes, dist-1

N = int(input())

answer = 0
jido = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if jido[i][j]==9:
            x, y = i, j
            jido[i][j]=0
shark_size = 2
cnt = 0

while True:
    fishes, dist = bfs(x, y)
    if len(fishes) == 0:
        break
    fishes.sort(key = lambda x: (x[0], x[1]))
    x, y = fishes[0]
    jido[x][y] = 0
    cnt += 1
    answer += dist
    if shark_size == cnt:
        shark_size += 1
        cnt = 0

print(answer)