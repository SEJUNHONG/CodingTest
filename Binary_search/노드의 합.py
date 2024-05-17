T = int(input())

def post_order(L):
    if L <= N:
        if visited[L] == 0:
            visited[L] = post_order(L*2) + post_order(L*2+1)
        return visited[L]
    else:
        return 0

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    visited = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        visited[a] = b

    print(f'#{t} {post_order(L)}')