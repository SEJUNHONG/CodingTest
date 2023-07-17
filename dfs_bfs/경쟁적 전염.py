from collections import deque

N, K = map(int, input().split())
graph = []
data = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
data.sort()
queue = deque(data)
S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while queue:
    virus, s, x, y = queue.popleft()
    if s == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(graph[X-1][Y-1])