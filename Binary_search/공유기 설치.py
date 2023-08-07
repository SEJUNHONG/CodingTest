N, C = map(int, input().split())
home = []
for _ in range(N):
    home.append(int(input()))
home.sort()

start = home[1] - home[0]
end = home[-1] - home[0]
answer = 0

while(start <= end):
    mid = (start + end) // 2
    value = home[0]
    cnt = 1

    for i in range(1, N):
        if home[i] >= value + mid:
            value = home[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid -1

print(answer)