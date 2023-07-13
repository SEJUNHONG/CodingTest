from itertools import combinations

N, M = map(int, input().split())
chicken, house = [], []

for r in range(N):
    jido = list(map(int, input().split()))
    #print(jido)
    for c in range(N):
        if jido[c] == 1:
            house.append((r, c))
        elif jido[c] == 2:
            chicken.append((r, c))

print(chicken)
peups = list(combinations(chicken, M))
print(peups)

def chicken_distance(peups):
    answer = 0
    for hx, hy in house:
        temp = 1e9
        for px, py in peups:
            temp = min(temp, abs(hx - px) + abs(hy - py))
        answer += temp

    return answer

answer = 1e9
for peup in peups:
    answer = min(answer, chicken_distance(peup))

print(answer)