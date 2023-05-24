people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    answer = 0
    p = sorted(people)
    i = 0
    j = len(people) - 1
    while i <= j:
        answer += 1
        if p[i] + p[j] <= limit:
            i += 1
        j -= 1
    return answer

print(solution(people, limit))
