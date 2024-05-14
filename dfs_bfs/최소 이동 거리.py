from collections import deque

T = int(input())

def bfs(s):
    q = deque()
    visited = [INF] * (N+1)

    q.append(s)
    visited[s] = 0

    while q:
        s = q.popleft()
        for (e, w) in adj[s]:
            if visited[e] > visited[s] + w:
                q.append(e)
                visited[e] = visited[s] + w
    return visited[N]

for test_case in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    INF = 1e9
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))

    print(f'#{test_case} {bfs(0)}')