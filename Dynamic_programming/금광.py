T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    chaegulji = list(map(int, input().split()))

    dp = []
    idx = 0
    for i in range(n):
        dp.append(chaegulji[idx:idx+m])
        idx += m
    
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m-1])
    print(answer)