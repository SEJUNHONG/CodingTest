import sys 
input = sys.stdin.readline

N, L = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def check(line, visited):
    cnt = 1
    for i in range(1, len(line)):
        if line[i-1] == line[i]:
            cnt += 1
        elif line[i-1]+1 == line[i] and cnt >= L and visited[i-L:i] == [0] * L:
            cnt = 1
            visited[i-L:i] = [1] * L
        elif line[i-1] > line[i]:
            cnt = 1
        else:
            return False
    return True 


for _ in range(2):
    for line in jido:
        visited = [0] * len(line)
        if check(line, visited) and check(line[::-1], visited[::-1]):
            answer += 1
    jido = list(map(list, zip(*jido)))

print(answer)