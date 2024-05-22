cogwheel = [[0] * 8] + [list(map(int, input())) for _ in range(4)]
K = int(input())
top = [0] * 5

for _ in range(K):
    idx, direction = map(int, input().split())

    temp_list = [(idx, 0)]

    for i in range(idx+1, 5):
        if cogwheel[i-1][(top[i-1]+2)%8] != cogwheel[i][(top[i]+6)%8]:
            temp_list.append((i, (i-idx)%2))
        else:
            break

    for i in range(idx-1, 0, -1):
        if cogwheel[i][(top[i]+2)%8] != cogwheel[i+1][(top[i+1]+6)%8]:
            temp_list.append((i, (idx-i)%2))
        else:
            break
    for i, rot in temp_list:
        if rot == 0:
            top[i] = (top[i] - direction + 8) % 8
        else:
            top[i] = (top[i] + direction + 8) % 8

answer = 0
score = [0, 1, 2, 4, 8]
for i in range(1, 5):
    answer += cogwheel[i][top[i]] * score[i]
print(answer)