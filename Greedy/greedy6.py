S = str(input())

num0, num1 = 0, 0

if S[0] =='1':
    num0 += 1
else:
    num1 += 1

for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            num0 += 1
        else:
            num1 += 1
print(min(num0, num1))

