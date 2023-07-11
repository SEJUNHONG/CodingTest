N = int(input())
K = int(input())
jido = [[0] * (N+1) for _ in range(N+1)]
directions = []

for _ in range(K):
    i, j = map(int, input().split())
    jido[i][j] = 1

L = int(input())
for _ in range(L):
    X, C = input().split()
    directions.append((int(X), C))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, C):
    if C == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def solution():
    x, y = 1, 1
    jido[x][y] = 2
    direction = 0
    time = 0
    idx = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= N and 1 <= ny <= N and jido[nx][ny] != 2:
            if jido[nx][ny] == 0:
                jido[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                jido[px][py] = 0

            if jido[nx][ny] == 1:
                jido[nx][ny] = 2
                q.append((nx, ny))

        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        if idx < 1 and time == directions[idx][0]:
            direction = turn(direction, directions[idx][1])
            idx += 1

    return time

print(solution())