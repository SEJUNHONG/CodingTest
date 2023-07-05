s = 'xababcdcdababcdcd' #'abcabcabcabcdededededede' #'abcabcdede' #'ababcdcdababcdcd' #'aabbaccc'

def solution(s):
    K = int(len(s)/2)
    answer = len(s)
    for k in range(1, K+1):
        comp = ""
        prev = s[0:k]
        count = 1
        for j in range(k, len(s), k):
            if prev == s[j:j+k]:
                count += 1
            else:
                comp += str(count) + prev if count >= 2 else prev
                prev = s[j:j+k]
                count = 1
        comp += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(comp))
    return answer

print(solution(s))