N = int(input())
A_N = list(map(int, input().split()))
plus, minus, times, division = map(int, input().split())

maximum, minimum = -1e9, 1e9

def dfs(i, now):
    global minimum, maximum, plus, minus, times, division

    if i == N:
        minimum = min(minimum, now)
        maximum = max(maximum, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now + A_N[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now - A_N[i])
            minus += 1
        if times > 0:
            times -= 1
            dfs(i+1, now * A_N[i])
            times += 1
        if division > 0:
            division -= 1
            dfs(i+1, int(now / A_N[i]))
            division += 1

dfs(1, A_N[0])

print(maximum)
print(minimum)