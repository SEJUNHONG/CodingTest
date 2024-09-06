def dfs(n, cnt):
    global answer

    if answer >= (cnt+(L+1-n)//2):
        return

    if n >= L:
        answer = max(answer, cnt)
        return

    for x, y in visited[n]:
        if v[x-y] == 0:
            v[x-y] = 1
            dfs(n+2, cnt+1)
            v[x-y] = 0
    dfs(n+2, cnt)

N = int(input())
boards = [list(map(int, input().split())) for _ in range(N)]
visited = [[] for _ in range(2*N)]
for i in range(N):
    for j in range(N):
        if boards[i][j] == 1:
            visited[i+j].append((i, j))
L = 2*N - 1
v = [0]*(2*N)
answer = 0
dfs(0, 0)
t = answer
answer = 0
dfs(1, 0)
print(answer + t)

