def bfs(start, end):
    q = []
    visited = [0] * 200001

    q.append(start)
    visited[start] = 1
    while q:
        now = q.pop(0)
        if now == end:
            return visited[end] - 1
        for next in (now-1, now+1, now*2):
            if 0 <= next <= 200000 and visited[next] == 0:
                q.append(next)
                visited[next] = visited[now] + 1
    return -1

N, K = map(int, input().split())
answer = bfs(N, K)
print(answer)