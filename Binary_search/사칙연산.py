def post_order(n):
    if lst[n]:
        if lst[n] == '+':
            return post_order(ch1[n]) + post_order(ch2[n])
        elif lst[n] == '-':
            return post_order(ch1[n]) - post_order(ch2[n])
        elif lst[n] == '*':
            return post_order(ch1[n]) * post_order(ch2[n])
        elif lst[n] == '/':
            return post_order(ch1[n]) / post_order(ch2[n])
        else:
            return int(lst[n])
    else:
        return 0

T = 10
for t in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for _ in range(N):
        tlst = input().split()
        idx = int(tlst[0])
        lst[idx] = tlst[1]
        if len(tlst) > 2:
            ch1[idx] = int(tlst[2])
            ch2[idx] = int(tlst[3])

    ans = int(post_order(1))
    print(f'#{t} {ans}')