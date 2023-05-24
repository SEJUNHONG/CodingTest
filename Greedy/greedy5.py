S = input()

answer = 0
for s in S:
    num = int(s)
    if num <= 1 or answer <= 1:
        answer += num
    else:
        answer *= num

print(answer)