N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

target = 1
for x in num_list:
    if target < x:
        break
    target += x

print(target)