K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate(arr, x, y):
    rot_arr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            rot_arr[x+i][y+j] = arr[x+3-j-1][y+i]
    return rot_arr

def bfs(arr, visited, x, y, clear):
    q = []
    sset = set()
    cnt = 0

    q.append((x, y))
    visited[x][y] = 1
    sset.add((x, y))
    cnt += 1

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and arr[x][y] == arr[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                sset.add((nx, ny))
                cnt += 1
    if cnt >= 3:
        if clear == 1:
            for x, y in sset:
                arr[x][y] = 0
        return cnt
    else:
        return 0
def count_clear(arr, clear):
    visited = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                temp = bfs(arr, visited, i, j , clear)
                cnt += temp
    return cnt

for _ in range(K):
    max_cnt = 0
    for rot in range(1, 4):
        for x in range(3):
            for y in range(3):
                rot_arr = [x[:] for x in arr]
                for _ in range(rot):
                    rot_arr = rotate(rot_arr, x, y)

                temp = count_clear(rot_arr, 0)
                if max_cnt < temp:
                    max_cnt = temp
                    new_arr = rot_arr

    if max_cnt == 0:
        break

    cnt = 0
    arr = new_arr
    while True:
        temp = count_clear(arr, 1)
        if temp == 0:
            break
        cnt += temp

        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)

    answer.append(cnt)
print(*answer)