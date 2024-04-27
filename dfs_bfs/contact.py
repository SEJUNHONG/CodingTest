from collections import deque
T = 10

def bfs(S):
    q = deque()
    visited = [0] * 101
    q.append(S)
    visited[S] = 1
    answer = S

    while q:
        now = q.popleft()
        if visited[answer] < visited[now] or (visited[answer] == visited[now] and answer < now):
            answer = now

        for next in adj[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now] + 1
    return answer

for test_case in range(1, T+1):
    length, S = map(int, input().split())
    adj = [[] for _ in range(101)]
    lst = list(map(int, input().split()))
    for i in range(0, length, 2):
        start, end = lst[i], lst[i+1]
        adj[start].append(end)

    print(f'#{test_case} {bfs(S)}')