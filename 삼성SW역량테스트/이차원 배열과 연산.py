import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1
jido = [list(map(int, input().split())) for _ in range(3)]

for answer in range(101):
    if 0 <= r < len(jido) and 0 <= c < len(jido[0]) and jido[r][c] == k:
        break
    
    r_cal = 1
    if len(jido) < len(jido[0]):
        r_cal = 0
        jido = list(map(list, zip(*jido)))

    max_col = 0
    for i in range(len(jido)):
        cnts = {}
        for j in range(len(jido[i])):
            if jido[i][j] == 0: continue
            if jido[i][j] in cnts:
                cnts[jido[i][j]] += 1
            else:
                cnts[jido[i][j]] = 1
        lsts = sorted(cnts.items(), key = lambda x:(x[1], x[0]))
        
        jido[i] = [n for lst in lsts for n in lst]
        max_col = max(max_col, len(jido[i]))
    
    max_col = min(max_col, 100)
    for i in range(len(jido)):
        while len(jido[i]) < max_col:
            jido[i].append(0)
        while len(jido[i]) > max_col:
            jido[i].pop()

    if r_cal == 0:
        jido = list(map(list, zip(*jido)))
else:
    answer -= 1

print(answer)