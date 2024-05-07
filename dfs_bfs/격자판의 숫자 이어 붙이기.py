from collections import deque
T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(n, num, x, y):
    if n == 7:
        answer.add(num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(n+1, num*10+grid[nx][ny], nx, ny)

for test_case in range(1, T+1):
    grid = [list(map(int, input().split())) for _ in range(4)]

    answer = set()
    for i in range(4):
        for j in range(4):
            dfs(1, grid[i][j], i, j)

    print(f'#{test_case} {len(answer)}')