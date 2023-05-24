N, M = map(int, input().split())
num_list = list(map(int, input().split()))
answer = 0
for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] == num_list[j]:
            continue
        else:
            answer += 1
print(answer)