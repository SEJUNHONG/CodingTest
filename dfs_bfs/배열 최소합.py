T = int(input())

def dfs(n, temp):
    global answer
    if answer <= temp:
        return

    if n == N:
        answer = min(answer, temp)
        return

    for j in range(N):
        if visited[j] == False:
            visited[j] = True
            dfs(n+1, temp+arr[n][j])
            visited[j] = False

for test_case in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))

    answer = N*10
    visited = [False] * N
    dfs(0, 0)

    print(f'#{test_case} {answer}')
