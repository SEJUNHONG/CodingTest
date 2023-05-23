N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()
num1 = num_list[-1]
num2 = num_list[-2]

answer = 0

while True:
    for j in range(K):
        if M == 0:
            break
        answer += num1
        M -= 1
    if M == 0:
        break
    answer += num2
    M -= 1

print(answer)