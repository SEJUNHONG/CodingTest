N = int(input())
num_list = list(map(int, input().split()))

fixed = 0
for idx, num in enumerate(num_list):
    if idx == num:
        fixed = num

if fixed == 0:
    fixed = -1
    print(fixed)
else:
    print(fixed)