N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
classroom = [[0] * N for _ in range(N)]
sorted_students = [[0]*5] + sorted(students)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for student in students:
    mx = empty_mx = -1
    for x in range(N):
        for y in range(N):
            if classroom[x][y] > 0:
                continue
            cnt = empty_cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] in student:
                    cnt += 1
                if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] == 0:
                    empty_cnt += 1
            if mx < cnt or mx == cnt and empty_mx < empty_cnt:
                mx, empty_mx = cnt, empty_cnt
                ex, ey = x, y
    classroom[ex][ey] = student[0]

table = [0, 1, 10, 100, 1000]
answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] in sorted_students[classroom[i][j]]:
                cnt += 1
        answer += table[cnt]
print(answer)