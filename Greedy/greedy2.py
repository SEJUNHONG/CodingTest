N, M = map(int, input().split())
temp = 0
for _ in range(N):
    temp = max(temp, min(list(map(int, input().split()))))
print(temp)