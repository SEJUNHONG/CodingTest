import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))

robot = [0] * N
answer = 0
cnt = 0

while True:
    answer += 1
    belt = [belt[-1]] + belt[:-1]
    robot = [0] + robot[:-1]
    robot[N-1] = 0

    for i in range(N-2, 0, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i], robot[i+1] = 0, 1
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1
    
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1

    if cnt >= K:
        break

print(answer)
