answers = [1,3,2,4,2]

def solution(answers):
    answer = []
    p1 = [1,2,3,4,5] * 250
    p2 = [2,1,2,3,2,4,2,5] * 125
    p3 = [3,3,1,1,2,2,4,4,5,5] * 100
    a1, a2, a3 = 0, 0, 0
    
    for i in range(len(answers)) :
        if answers[i] == p1[i%5] :
            a1 += 1
        if answers[i] == p2[i%8] :
            a2 += 1
        if answers[i] == p3[i%10] :
            a3 += 1
    
    if a1 == max(a1, a2, a3) :
        answer.append(1)
    if a2 == max(a1, a2, a3):
        answer.append(2)
    if a3 == max(a1, a2, a3):
        answer.append(3)

    return answer

print(solution(answers))