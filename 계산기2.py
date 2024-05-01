T = 10
op = {'+':1, '*':2}
for test_case in range(1, T+1):
    length = int(input())
    calculate = input()

    equation = ''
    stack = []

    for char in calculate:
        if char.isdigit():
            equation += char
        else:
            while stack and op[char] <= op[stack[-1]]:
                equation += stack.pop()
            stack.append(char)
    while stack:
        equation += stack.pop()

    for char in equation:
        if char.isdigit():
            stack.append(int(char))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '*':
                stack.append(op1*op2)
            elif char == '+':
                stack.append(op1+op2)

    print(f'#{test_case} {stack.pop()}')
