def dfs(n, cnt):
    global answer
    if answer >= (cnt + (N - n)*2):
        return

    if n == N:
        answer = max(answer, cnt)
        return

    if eggs[n][0] <= 0:
        dfs(n+1, cnt)
    else:
        flag = False
        for j in range(N):
            if n == j or eggs[j][0] <= 0:
                continue
            flag = True
            eggs[n][0] -= eggs[j][1]
            eggs[j][0] -= eggs[n][1]
            dfs(n+1, cnt + int(eggs[n][0] <= 0)+int(eggs[j][0]<=0))
            eggs[n][0] += eggs[j][1]
            eggs[j][0] += eggs[n][1]
        if flag == False:
            dfs(n+1, cnt)

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dfs(0, 0)
print(answer)