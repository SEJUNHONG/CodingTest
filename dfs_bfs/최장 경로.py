T = int(input())

def dfs(c, v):
    global answer
    answer = max(answer, len(v))

    for n in visited[c]:
        if n not in v:
            dfs(n, v+[n])

for x in range(1, T):
    answer = 0
    N, M = map(int, input().split())
    visited = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end = map(int, input().split())
        visited[start].append(end)
        visited[end].append(start)
    for s in range(1, N+1):
        dfs(s, [s])
    print(f'#{x} {answer}')