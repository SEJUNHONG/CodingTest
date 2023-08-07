N = int(input())
parts = list(map(int, input().split()))
M = int(input())
part = list(map(int, input().split()))

for i in part:
    a = len(parts)
    for j in parts:
        if i == j:
            print("yes")
        else:
            a -= 1
    if a == 0:
        print("no")
    