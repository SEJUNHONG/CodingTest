N = int(input())
T_sum = []
P_sum = []
dp = [0] * (N+1)
max_value = 0

for _ in range(N):
    T, P = map(int, input().split())
    T_sum.append(T)
    P_sum.append(P)

for i in range(N-1, -1, -1):
    time = T_sum[i] + i
    if time <= N:
        dp[i] = max(P_sum[i] + dp[time], max_value)
        max_value = dp[i]

    else:
        dp[i] = max_value

print(max_value)