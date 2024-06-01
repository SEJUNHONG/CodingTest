import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

for _ in range(M):  
    d_i, s_i = map(int, input().split())

    next_cloud = []
    for x, y in cloud:
        nx = (x + dx[d_i] * s_i + N) % N
        ny = (y + dy[d_i] * s_i + N) % N

        jido[nx][ny]+=1    
        next_cloud.append((nx,ny))

    v = [[0]*N for _ in range(N)]
    for x, y in next_cloud:
        v[x][y] = 1
        for d_xx, d_yy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            nx, ny = x + d_xx, y + d_yy
            if 0 <= nx < N and 0 <= ny < N and jido[nx][ny] > 0:
                jido[x][y] += 1


    cloud = []
    for i in range(N):
        for j in range(N):
            if jido[i][j] >= 2 and v[i][j] == 0:
                jido[i][j] -= 2
                cloud.append((i, j))

answer = 0 
for water in jido:
    answer += sum(water)

print(answer)

