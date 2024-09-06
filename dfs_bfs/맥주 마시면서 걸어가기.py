def bfs(sx, sy, ex, ey):
    q = []
    visited = [0] * n

    q.append((sx, sy))

    while q:
        x, y = q.pop(0)
        if abs(x - ex) + abs(y - ey) <= 1000:
            return 'happy'

        for i in range(n):
            if visited[i] == 0:
                nx, ny = locations[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append((nx, ny))
                    visited[i] = 1
    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    locations = []
    for i in range(n):
        x, y = map(int, input().split())
        locations.append((x, y))
    ex, ey = map(int, input().split())

    print(bfs(sx, sy, ex, ey))