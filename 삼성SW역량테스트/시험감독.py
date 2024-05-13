N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in range(len(A)):
    if A[i] <= B:
        answer += 1
    else:
        answer += 1
        if (A[i] - B) % C == 0:
            answer += int((A[i] - B) / C)
        else:
            answer += int((A[i] - B) / C + 1)

print(answer)
