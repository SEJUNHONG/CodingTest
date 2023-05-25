sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    s1 = []
    s2 = []
    for s in sizes:
        if s[0] >= s[1]:
            s1.append(s[0])
            s2.append(s[1])
        else:
            s1.append(s[1])
            s2.append(s[0])
    answer = max(s1) * max(s2)
    return answer

print(solution(sizes))