from collections import deque

M, N = map(int, input().split())

tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                queue.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1

all = False
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            all = True
            break
if all:
    print(-1)
else:
    print(max(map(max, tomato))-1)