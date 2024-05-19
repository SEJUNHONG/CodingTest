N = int(input())
skill = [list(map(int, input().split())) for _ in range(N)]

M = N//2
answer = 100 * M * M

def cal(start, link):
    starts = links = 0
    for i in range(M):
        for j in range(M):
            starts += skill[start[i]][start[j]]
            links += skill[link[i]][link[j]]
    return abs(starts - links)

def dfs(n, start, link):
    global answer
    if n == N:
        if len(start) == len(link):
            answer = min(answer, cal(start, link))
        return 
    dfs(n+1, start+[n], link)
    dfs(n+1, start, link+[n])

dfs(0, [], [])
print(answer)