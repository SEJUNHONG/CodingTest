from collections import deque

R, C = map(int, input().split())
jido = [list(input()) for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, jido[0][0]))

    visited = [[set() for _ in range(C)] for _ in range(R)]
    visited[0][0].add(jido[0][0])
    answer = 1

    while q:
        x, y, v = q.popleft()
        answer = max(answer, len(v))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and jido[nx][ny] not in v:
                if v + jido[nx][ny] not in visited[nx][ny]:
                    visited[nx][ny].add((v+jido[nx][ny]))
                    q.append((nx, ny, v+jido[nx][ny]))
    return answer

print(bfs())
