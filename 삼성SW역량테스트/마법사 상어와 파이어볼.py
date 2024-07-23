import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

skill = [list(map(int, input().split())) for _ in range(M)]

for _ in range(K):
    for i in range(len(skill)):
        skill[i][0] = (skill[i][0] + dx[skill[i][4] * skill[i][3]]) % N + 1
        skill[i][1] = (skill[i][1] + dy[skill[i][4] * skill[i][3]]) % N + 1
    skill.sort(key = lambda x:(x[0], x[1]))
    skill.append([100,100,0,0,0])
    new = []

    i = 0
    while i < len(skill) -1 :
        r, c, m, d, s = skill[i]
        start = 0
        for j in range(i+1, len(skill)):
            if (r, c) == (skill[j][0], skill[j][1]):
                m += skill[j][2]
                s += skill[j][3]
                if d % 2 != skill[j][4] % 2:
                    start = 1
            else:
                if j-i == 1:
                    new.append(skill[i])
                else:
                    if m // 5 > 0:
                        for dr in range(start, start+8, 2):
                            new.append([r, c, m//5, s//(j-i), d])
                break
        i=j
    skill = new
answer = 0
for lst in skill:
    answer += lst[2]

print(answer)