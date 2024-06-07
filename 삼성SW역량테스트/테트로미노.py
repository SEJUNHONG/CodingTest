import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(N, sm, tlist):
    global answer
    if sm+(4-N)*mx <= answer:
        return
    
    if N == 4:
        answer = max(answer, sm)
        return 
    
    for x, y in tlist:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(N+1, sm+jido[nx][ny], tlist+[(nx, ny)])
                visited[nx][ny] = False

answer = 0
mx = max(map(max, jido))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, jido[i][j], [(i, j)])

print(answer)
