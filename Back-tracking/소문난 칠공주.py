from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    v = [[0]*5 for _ in range(5)]

    q.append((x, y))
    v[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny <5 and v[nx][ny] == 0 and visited[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = 1
                cnt += 1
    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                return bfs(i, j)

def dfs(n, cnt, scnt):
    global answer
    if cnt > 7:
        return

    if n == 25:
        if cnt == 7 and scnt >= 4:
            if check():
                answer += 1
        return

    visited[n//5][n%5] = 1
    dfs(n+1, cnt+1, scnt+int(students[n//5][n%5] == 'S'))
    visited[n//5][n%5] = 0
    dfs(n+1, cnt, scnt)

students = [input() for _ in range(5)]
answer = 0
visited = [[0]*5 for _ in range(5)]
dfs(0, 0, 0)
print(answer)