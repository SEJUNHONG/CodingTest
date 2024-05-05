from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    ans = []

    q.append((x, y))
    visited[x][y] = 1
    ans.append(rooms[x][y])


    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if abs(rooms[nx][ny] - rooms[x][y]) == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    ans.append((rooms[nx][ny]))
    return min(ans), len(ans)

for test_case in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N  for _ in range(N)]
    start, answer = N*N, 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                temp_start, temp_answer = bfs(i, j)
                if answer < temp_answer or (answer == temp_answer and start > temp_start):
                    start, answer = temp_start, temp_answer

    print(f'#{test_case} {start} {answer}')