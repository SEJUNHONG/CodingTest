from collections import deque

T = int(input())

operation = [1, -1, 2, -10]

def bfs(N, M):
    q = deque()
    q.append(N)

    visited = [0] * 1000001
    visited[N] = 1

    while q:
        x = q.popleft()
        if x == M:
            return visited[x] - 1

        for i in range(4):
            if i == 2:
                nx = x * operation[i]
            else:
                nx = x + operation[i]
            if 1 <= nx <= 1000000 and visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1
    return -1

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{test_case} {bfs(N, M)}')