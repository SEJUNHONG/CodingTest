import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
cctv_p = []
cctv = [[], [1], [1,3], [0,1], [0,1,3], [0,1,2,3]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if 1 <= jido[i][j] <=5:
            cctv_p.append((i, j))


def cal(tlst):
    visited = [[0] * M for _ in range(N)]
    for i in range(cnt):
        x, y = cctv_p[i]
        rot = tlst[i]
        type = jido[x][y]

        for dr in cctv[type]:
            dr = (dr + rot) % 4
            while True:
                nx = x + dx[dr]
                ny = y + dy[dr]
                if jido[nx][ny] == 6:
                    break
                if 0 <= nx < N and 0 <= ny < M:
                    visited[nx][ny] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if jido[i][j] == 0 and visited[i][j] == 0:
                ans += 1
    return ans

def dfs(n, tlst):
    global answer
    if n == cnt:
        answer = min(answer, cal(tlst))
        return 
    
    dfs(n+1, tlst+[0])
    dfs(n+1, tlst+[1])
    dfs(n+1, tlst+[2])
    dfs(n+1, tlst+[3])

cnt = len(cctv_p)
answer = N * M
dfs(0, [])
print(answer)
