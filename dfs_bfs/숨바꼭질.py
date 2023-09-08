from collections import deque

MAX = 100001
visited = [0] * MAX

def bfs(N):
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break

        for i in (x-1, x+1, x*2):
            if 0 <= i < MAX and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

N, K = map(int, input().split())
bfs(N)