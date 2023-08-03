N = int(input())
num_array = []
for _ in range(N):
    num_array.append(int(input()))

num_array = sorted(num_array, reverse=True)

for i in num_array:
    print(i, end=' ')