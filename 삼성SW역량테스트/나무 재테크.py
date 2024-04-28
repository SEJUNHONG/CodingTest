N, M, K = map(int, input().split())

neutrition = [[5] * (N) for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
tree_age = [[[] for _ in range(N)] for _ in range(N)]
answer = 0
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree_age[x-1][y-1].append(z)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            tree_age[i][j].sort()
            for k in range(len(tree_age[i][j])):
                if neutrition[i][j] >= tree_age[i][j][k]:
                    neutrition[i][j] -= tree_age[i][j][k]
                    tree_age[i][j][k] += 1
                else:
                    while k < len(tree_age[i][j]):
                        neutrition[i][j] += (tree_age[i][j].pop() // 2)
                    break

    for i in range(N):
        for j in range(N):
            for k in range(len(tree_age[i][j])):
                if tree_age[i][j][k] % 5 == 0:
                    for l in range(8):
                        ni, nj = i + di[l], j + dj[j]
                        if 0 <= ni < N and 0 <= nj < N:
                            tree_age[ni][nj].append(1)

    for i in range(N):
        for j in range(N):
            neutrition[i][j] += A[i][j]

for i in range(N):
    for j in range(N):
        answer += len(tree_age[i][j])

print(answer)