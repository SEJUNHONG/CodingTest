from collections import deque

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, target_x, target_y):
    q = deque()
    q.append((x, y))

    visited = [[INF]*N for _ in range(N)]
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]>visited[x][y]+1+max(jido[nx][ny]-jido[x][y], 0):
                visited[nx][ny] = visited[x][y] + 1 + max(jido[nx][ny] - jido[x][y], 0)
                q.append((nx, ny))
    return visited[target_x][target_y]

for tc in range(1, T+1):
    N = int(input())
    jido = [list(map(int, input().split())) for _ in range(N)]
    INF = 1e9

    print(f'#{tc} {bfs(0, 0, N-1, N-1)}')