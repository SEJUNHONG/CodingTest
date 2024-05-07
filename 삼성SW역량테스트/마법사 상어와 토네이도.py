N = int(input())
sands = [list(map(int, input().split())) for _ in range(N)]

tx = [[-1, 1, -1, 1, 0, -2, 2, -1, 1, 0],
      [1, 1, 0, 0, 2, 0, 0, -1, -1, 1],
      [1, -1, 1, -1, 0, 2, -2, 1, -1, 0],
      [-1, -1, 0, 0, -2, 0, 0, 1, 1, -1]]

ty = [[-1, -1, 0, 0, -2, 0, 0, 1, 1, -1],
      [-1, 1, -1, 1, 0, -2, 2, -1, 1, 0],
      [1, 1, 0, 0, 2, 0, 0, -1, -1, 1],
      [1, -1, 1, -1, 0, 2, -2, 1, -1, 0]]

power = [10, 10, 7, 7, 5, 2, 2, 1, 1, 0]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt_max = 1
x, y = N//2, N//2
answer = dir = cnt = flag = 0
while (x, y) != (0, 0):
    x, y = x + dx[dir], y + dy[dir]
    if sands[x][y] > 0:
        sand = sands[x][y]
        sands[x][y] = sm = 0

        for i in range(10):
            nx, ny = x + tx[dir][i], y + ty[dir][i]
            temp = (sand * power[i]) // 100
            if i == 9:
                temp = sand - sm

            if 0 <= nx < N and 0 <= ny < N:
                sands[nx][ny] += temp
            else:
                answer += temp
            sm += temp

    cnt += 1
    if cnt == cnt_max:
        cnt = 0
        dir = (dir+1) % 4
        if flag == 0:
            flag = 1
        else:
            flag = 0
            cnt_max += 1

print(answer)

