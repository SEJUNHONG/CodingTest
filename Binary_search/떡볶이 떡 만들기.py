N, M = map(int, input().split())
ddeok = list(map(int, input().split()))

start = 0
end = max(ddeok)

answer = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in ddeok:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)