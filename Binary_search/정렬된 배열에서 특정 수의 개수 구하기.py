N, x = map(int, input().split())
sooyeol = list(map(int, input().split()))

answer = 0

for i in sooyeol:
    if i == x:
        answer += 1

if answer == 0:
    answer = -1
print(answer)