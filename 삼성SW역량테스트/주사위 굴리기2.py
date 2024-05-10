N, M, K = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d1, d2, d3, d4, d5, d6 = 1, 2, 3, 4, 5, 6
dir = 1
x, y = 0, 0
answer = 0

def bfs(x, y, sm):
    q = []
    visited = [[0]*M for _ in range(N)]

    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and jido[nx][ny] == sm:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

for _ in range(K):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
    else:
        dir = (dir + 2) % 4
        x, y = x + dx[dir], y + dy[dir]

    if dir == 0:
        d2, d1, d5, d6 = d1, d5, d6, d2
    elif dir == 1:
        d6, d4, d1, d3 = d3, d6, d4, d1
    elif dir == 2:
        d2, d1, d5, d6 = d6, d2, d1, d5
    else:
        d6, d4, d1. d3 = d4, d1, d3, d6

    answer += bfs(x, y, jido[x][y]) * jido[x][y]

    if d6 > jido[x][y]:
        dir = (dir+1) % 4
    elif d6 < jido[x][y]:
        dir = (dir-1) % 4
print(answer)