numbers = [4,1,2,1] # [1,1,1,1,1]
target = 4 # 3

def solution(numbers, target):
    answer = 0
    N = len(numbers)

    def dfs(idx, result):
        if idx == N:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])

    dfs(0, 0)

    return answer

print(solution(numbers, target))