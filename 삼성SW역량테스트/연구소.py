import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []
for i in range(N):
    for j in range(M):
        if jido[i][j] == 0:
            empty.append((i, j))
        elif jido[i][j] == 2:
            virus.append((i, j))

cnt = len(empty)
visited = [0] * cnt
answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(tlst):

    for i, j in tlst:
        jido[i][j] = 1

    q = deque()
    v = [[0] * M for _ in range(N)]
    cnts = cnt - 3

    for i, j in virus:
        q.append((i, j))
        v[i][j] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and jido[nx][ny] == 0 and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = 1
                cnts -= 1

    for i, j in tlst:
        jido[i][j] = 0

    return cnts

for i in range(cnt -2):
    for j in range(i+1, cnt-1):
        for k in range(j+1, cnt):
            answer = max(answer, bfs([empty[i], empty[j], empty[k]]))

print(answer)
