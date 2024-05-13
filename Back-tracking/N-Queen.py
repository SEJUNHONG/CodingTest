T = int(input())

def dfs(n):
    global answer
    if n == N:
        answer += 1
        return

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

for test_case in range(1, T+1):
    N = int(input())
    answer = 0

    v1, v2, v3 = [[0]*(2*N) for _ in range(3)]
    dfs(0)

    print(f'#{test_case} {answer}')