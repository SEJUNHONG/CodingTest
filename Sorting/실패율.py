N = 4 # 5
stages = [4,4,4,4,4] # [2,1,2,6,2,4,3,3]

def solution(N, stages):
    answer = []
    temp = []
    survive = len(stages)
    for i in range(1, N+1):
        fail = 0
        for j in range(len(stages)):
            if i == stages[j]:
                fail += 1            
        temp.append((i, fail/survive))
        survive -= fail
    temp = sorted(temp, key=lambda x:-x[1])
    for i in temp:
        answer.append(i[0])
    return answer

print(solution(N, stages))