n = int(input())
human1, human2 = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split())
    adj[parent].append(child)
    adj[child].append(parent)

def bfs(human1, human2):
    q = []
    visited = [0] * (n+1)

    q.append(human1)
    visited[human1] = 1

    while q:
        now = q.pop(0)
        if now == human2:
            return visited[human2] - 1
        for next in adj[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now] + 1
    return -1

answer = bfs(human1, human2)
print(answer)
