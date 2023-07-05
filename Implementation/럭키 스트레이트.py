num = input()
K = len(num)
num1, num2 = 0, 0
for i in range(int(K/2)):
    num1 += int(num[i])
    num2 += int(num[int(K/2)+i])

if num1 == num2:
    print('LUCKY')
else:
    print('READY')