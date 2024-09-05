from collections import deque

def bfs(S):
    global answer
    q = deque()
    visited = [0]*(F+1)
    q.append(S)
    visited[S] = 1

    while q:
        S = q.popleft()
        if S == G:
            return visited[S] - 1
        for i in range(2):
            nS = S + ds[i]
            if 1 <= nS <= F and visited[nS] == 0:
                q.append(nS)
                visited[nS] = visited[S] + 1
    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
ds = [U, -D]
print(bfs(S))