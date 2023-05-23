N = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

answer = 0
count = 0

for i in num_list:
    count += 1
    if count >= i:
        answer += 1
        count = 0

print(answer)