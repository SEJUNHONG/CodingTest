N = int(input())
arr = [[0] * 101 for _ in range(101)]

dx = [0, -1, 0 , 1]
dy = [1, 0, -1, 0]
answer = 0

for _ in range(N):
    y, x, d, g = map(int, input().split())
    lst = [(x, y)]
    lst.append((x+dx[d], y+dy[d]))
    for _ in range(g):
        end_x, end_y = lst[-1]
        for i in range(len(lst)-2, -1, -1):
            current_x, current_y = lst[i]
            lst.append((end_x - (end_y - current_y), end_y+(end_x - current_x)))

    for i, j in set(lst):
        arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1] == 1:
            answer += 1
print(answer)