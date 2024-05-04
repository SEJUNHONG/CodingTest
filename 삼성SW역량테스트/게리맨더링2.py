N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y, d1, d2):
    visited = [[0]*N for _ in range(N)]
    ans = [0] * 5

    visited[x][y] = 1
    j1 = j2 = y
    for dx in range(1, d1+d2+1):
        if dx <= d1:
            j1 -= 1
        else:
            j1 += 1

        if dx <= d2:
            j2 += 1
        else:
            j2 -= 1
        visited[x+dx][j1:j2+1] = [1] * (j2-j1+1)

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            if i < x+d1 and j <= y:
                ans[0] += A[i][j]
            if i <= x+d2 and y < j:
                ans[1] += A[i][j]
            if x+d1 <= i and j < y-d1+d2:
                ans[2] += A[i][j]
            if x + d2 < i and y-d1+d2 <=j:
                ans[3] += A[i][j]
    ans[4] = total - sum(ans)
    return max(ans) - min(ans)

total = sum(map(sum, A))
answer = 100 * N * N

for x in range(N-2):
    for y in range(1, N-1):
        for d1 in range(1, N):
            if 0 <= x+d1 < N and 0 <= y-d1 < N:
                for d2 in range(1, N):
                    if 0 <= x+d1+d2 < N and y+d2 < N:
                        answer = min(answer, dfs(x, y, d1, d2))

print(answer)