from collections import deque
from itertools import combinations

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    flower = 0
    while q:
        y, x, y_last, x_last, time, color = q.popleft()
        if visited[y_last][x_last] == 1:
            continue
        if visited[y][x]:
            if visited[y][x] == (time, -color):
                visited[y][x] = 1
                flower += 1
            continue
        visited[y][x] = (time, color)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N and grounds[ny][nx]:
                q.append((ny, nx, y, x, time+1, color))
    return flower

N, M, G, R = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]

candidates = []

for i in range(N):
    for j in range(M):
        if grounds[i][j] == 2:
            candidates.append((i, j))

answer = 0
for candidate in combinations(candidates, G+R):
    for g_candidate in combinations(candidate, G):
        visited = [[0]*M for _ in range(N)]
        q = deque()
        for y, x in g_candidate:
            visited[y][x] = 1
            q.append((y, x, y, x, 1, 1))
        for y, x in candidate:
            if visited[y][x]:
                continue
            q.append((y, x, y, x, 1, -1))
        visited = [[0]*M for _ in range(N)]
        answer = max(answer, bfs())
print(answer)