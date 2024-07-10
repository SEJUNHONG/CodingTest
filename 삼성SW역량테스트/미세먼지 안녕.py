import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(C)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(R):
    if jido[i][0] == -1:
        x1, x2 = i, i+1
        jido[x1][0] = jido[x2][0] = 0
        break

for _ in range(T):
    jido_t = [x[:] for x in jido]

    for x in range(R):
        for y in range(C):
            if jido[x][y] > 4:
                t = jido[x][y] // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) != (x1, 0) and (nx, ny) != (x2, 0):
                        jido_t[x][y] -= t
                        jido_t[nx][ny] += t

    jido = jido_t

    for i in range(x1-1, 0, -1):
        jido[i][0] = jido[i-1][0]
    for j in range(0, C-1, 1):
        jido[0][j] = jido[0][j+1]
    for i in range(0, x1, 1):
        jido[i][C-1] = jido[i+1][C-1]
    for j in range(C-1, 0, -1):
        jido[x1][j] = jido[x1][j-1]
    
    for i in range(x2+1, R-1, 1):
        jido[i][0] = jido[i+1][0]
    for j in range(0, C-1, 1):
        jido[R-1][j] = jido[R-1][j+1]
    for i in range(R-1, x2, -1):
        jido[i][C-1] = jido[i-1][C-1]
    for j in range(C-1, 0, -1):
        jido[x2][j] = jido[x2][j-1]

answer = sum(map(sum, jido))
print(answer)
