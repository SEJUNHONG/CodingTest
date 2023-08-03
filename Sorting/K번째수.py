array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])

    return answer

print(solution(array, commands))