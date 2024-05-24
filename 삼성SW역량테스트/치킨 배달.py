from itertools import combinations

N, M = map(int, input().split())
chicken, house = [], []
#jido = [list(map(int, input().split())) for _ in range(N)]
for r in range(N):
    jido = list(map(int, input().split()))
    for c in range(N):
        if jido[c] == 1:
            house.append((r, c))
        elif jido[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, M))

def distance(candidate):
    answer = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        answer += temp
    return answer

answer = 1e9
for candidate in candidates:
    answer = min(answer, distance(candidate))

print(answer)
