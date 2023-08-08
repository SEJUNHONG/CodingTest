N = 2 #5
number = 11 #12

def solution(N, number):
    answer = -1
    dp = [set() for i in range(8)]

    for i, num in enumerate(dp, 1):
        num.add(int(str(N) * i))
    
    for i in range(1, len(dp)):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            answer = i+1
            break
    else:
        answer -= 1
    return answer
print(solution(N, number))