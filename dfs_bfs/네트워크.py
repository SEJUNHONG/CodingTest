n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] #[[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def dfs(n, computers, com, visited):
    visited[com] = True
    for i in range(n):
        if i != com and computers[com][i] == 1:
            if visited[i] == False:
                dfs(n, computers, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            answer += 1

    return answer

print(solution(n, computers))