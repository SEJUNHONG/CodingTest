import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    union = [(x, y)]
    people = jido[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and L <= abs(jido[nx][ny] - jido[x][y]) <= R and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] =1
                union.append((nx, ny))
                people += jido[nx][ny]
    if len(union) > 1:
        for i, j in union:
            jido[i][j] = people // len(union)
        return 1
    return 0

while answer <= 2000:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                flag = max(flag, bfs(i, j))
    if flag == 0:
        break
    answer += 1

print(answer)