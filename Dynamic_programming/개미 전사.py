N = int(input())
siklyang = list(map(int, input().split()))

d = [0] * 100

d[0] = siklyang[0]
d[1] = max(siklyang[0], siklyang[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+siklyang[i])

print(d[N-1])