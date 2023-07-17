from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"] #["hot", "dot", "dog", "lot", "log", "cog"]	

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])
    V = [0 for i in range(len(words))]
    while queue:
        w, cnt = queue.popleft()
        if w == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(w)):
                    if w[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    queue.append([words[i], cnt+1])
                    V[i] = 1

    return answer

print(solution(begin, target, words))