def dfs(n):
    global answer
    v[n] = 1
    answer += 1

    for num in visited[n]:
        if not v[num]:
            dfs(num)

N = int(input())
M = int(input())
visited = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    visited[start].append(end)
    visited[end].append(start)
v = [0] * (N+1)
answer = 0
dfs(1)
print(answer - 1)