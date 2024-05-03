T = int(input())

def dfs(n, cnt, sm):
    global answer
    if answer <= cnt:
        return

    if n == N:
        answer = min(answer, cnt)
        return answer

    if sm > 0:
        dfs(n+1, cnt, sm-1)

    dfs(n+1, cnt+1, bus_stop[n]-1)

for test_case in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    N = bus_stop[0]
    answer = N

    dfs(2, 0, bus_stop[1]-1)

    print(f'#{test_case} {answer}')