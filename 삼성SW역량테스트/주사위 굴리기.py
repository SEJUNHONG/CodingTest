import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

n1 = n2 = n3 = n4 = n5 = n6 = 0
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

moves = list(map(int, input().split()))
answer = []

for move in moves:
    nx = x + dx[move]
    ny = y + dy[move]
    if 0 <= nx < N and 0 <= ny < M:
        if move == 1:
            n1, n3, n4, n6 = n4, n1, n6, n3
        elif move == 2:
            n1, n3, n4, n6 = n3, n6, n1, n4
        elif move == 3:
            n1, n2, n5, n6 = n5, n1, n6, n2
        elif move == 4:
            n1, n2, n5, n6 = n2, n6, n1, n5
            
        if jido[nx][ny] == 0:
            jido[nx][ny] = n6
        else:
            n6, jido[nx][ny] = jido[nx][ny], 0
        answer.append(n1)
        x, y = nx, ny
print(*answer, sep='\n')