def solution(n):
    answer = 0
    three = ''
    while n >= 3:
        three += str(n % 3)
        n = n // 3
    three += str(n)
    for i in range(len(three), 0, -1):
        answer += int(three[i-1]) * (3 ** (len(three) - i))
    return answer