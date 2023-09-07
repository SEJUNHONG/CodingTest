from collections import deque

dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1))

    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            print(visited[x][y] - 1)
            return True
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return False    

N = int(input())
for i in range(N):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    visited[x1][y1] = 1
    bfs(x1, y1, x2, y2)