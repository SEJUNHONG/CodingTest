def solution(n, left, right):
    answer = []
    for num in range(left, right+1):
        i = num//n
        j = num%n
        if i < j:
            i, j = j, i
        answer.append(i+1)
    return answer