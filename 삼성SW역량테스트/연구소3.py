from collections import deque

N, M = map(int, input().split())
jido =[list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
num = 0
for i in range(N):
    for j in range(N):
        if jido[i][j] == 2:
            virus.append((i, j))
        elif jido[i][j] == 0:
            num += 1

num_virus = len(virus)
answer = N * N

def bfs(virus_list):
    q = deque()
    visited = [[0] * N for _ in range(N)]

    for x, y in virus_list:
        q.append((x, y))
        visited[x][y] = 1

    cnt = num

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <N and 0 <= ny < N and visited[nx][ny] == 0 and jido[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] +1
                if jido[nx][ny] == 0:
                    cnt -=1
                    if cnt == 0:
                        return visited[nx][ny] - 1

    return N * N

def dfs(n, idx, virus_list):
    global answer
    if n == M:
        answer = min(answer, bfs(virus_list))
        return

    for j in range(idx, num_virus):
        dfs(n+1, j+1, virus_list+[virus[j]])
if num == 0:
    answer = 0
else:
    answer = N * N
    dfs(0, 0, [])
    if answer == N * N:
        answer = -1
print(answer)
