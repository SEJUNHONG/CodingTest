from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[False] * 16 for _ in range(16)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if miro[nx][ny] == 3:
                return 1
            if 0 <= nx < 16 and 0 <= ny < 16 and miro[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return 0



for _ in range(10):
    test_case = int(input())
    miro = [list(map(int, input())) for _ in range(16)]


    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                start_x, start_y = i, j
            if miro[i][j] == 3:
                end_x, end_y = i, j



    print(f'#{test_case} {bfs(1, 1)}')