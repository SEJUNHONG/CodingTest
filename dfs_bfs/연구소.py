N, M = map(int, input().split())
data = []
temp = [[0] * M for _ in range(N)]

for _ in range(N):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global answer
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j]

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)

        answer = max(answer, get_score())
        return
    
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(answer)