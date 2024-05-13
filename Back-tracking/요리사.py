T = int(input())

def dfs(n, A, B):
    global answer
    if n == N:
        if len(A) == M:
            Asum = Bsum = 0
            for i in range(M):
                for j in range(M):
                    Asum += foods[A[i]][A[j]]
                    Bsum += foods[B[i]][B[j]]
            answer = min(answer, abs(Asum-Bsum))
        return
    dfs(n+1, A+[n], B)
    dfs(n+1, A, B+[n])

for t in range(1, T+1):
    N = int(input())
    M = N//2
    foods = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e9

    dfs(0, [], [])

    print(f'#{t} {answer}')