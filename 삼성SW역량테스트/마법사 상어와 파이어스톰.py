from collections import deque

N, Q = map(int, input().split())
N = 2**N
ice = [list(map(int, input().split())) for _ in range(N)]
Ls = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for L in Ls:
    L = 2**L

    new = [[0]*N for _ in range(N)]
    for i in range(0, N, L):
        for j in range(0, N, L):
            for ni in range(L):
                for nj in range(L):
                    new[i+ni][j+nj] = ice[i+L-1-nj][j+ni]
    ice = new

    new = [x[:] for x in ice]
    for x in range(N):
        for y in range(N):
            if ice[x][y] == 0:
                continue
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and ice[nx][ny] == 0:
                    cnt += 1
                    if cnt >= 2:
                        new[x][y] -= 1
                        break
    ice = new

def bfs(x, y):
    q = []
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and ice[nx][ny] > 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

visited = [[0]*N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and ice[i][j] > 0:
            answer = max(answer, bfs(i, j))
print(sum(map(sum, ice)))
print(answer)