T = int(input())

def dfs(n, cnt, sm, x, y):
    global mx
    if cnt > C:
        return
    if n == M:
        mx = max(mx, sm)
        return
    dfs(n+1, cnt + arr[x][y+n], sm+arr[x][y+n]**2, x, y)
    dfs(n+1, cnt, sm, x, y)

for x in range(1, T+1):
    answer = 0
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = sm1 = 0
    for i1 in range(N):
        for j1 in range(N-M+1):
            mx = 0
            dfs(0, 0, 0, i1, j1)
            sm1 = mx
            for i2 in range(i1, N):
                sj = j1 + M if i1 == i2 else 0
                for j2 in range(sj, N-M+1):
                    mx = 0
                    dfs(0, 0, 0, i2, j2)
                    answer = max(answer, sm1+mx)

    print(f'#{x} {answer}')