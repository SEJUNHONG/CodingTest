N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

answer = 0
def dfs(n, sm):
    global answer
    if n >= N:
        answer = max(answer, sm)
        return 
    
    if n + T[n] <= N:
        dfs(n + T[n], sm + P[n])
    dfs(n+1, sm)

dfs(0, 0)
print(answer)