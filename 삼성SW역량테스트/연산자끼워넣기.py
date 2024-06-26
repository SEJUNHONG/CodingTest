N = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_num, min_num = -1e9, 1e9

def dfs(i, now):
    global max_num, min_num, add, sub, mul, div

    if i == N:
        min_num = min(min_num, now)
        max_num = max(max_num, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + num_list[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - num_list[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * num_list[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/num_list[i]))
            div += 1

dfs(1, num_list[0])

print(max_num)
print(min_num)
