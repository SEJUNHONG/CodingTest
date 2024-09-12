def solution(s):
    stack = []
    for i in s.split('},'):
        stack.append(i.replace('{','').replace('}','').split(','))
    stack.sort(key=len)
    answer = []
    for i in stack:
        for j in i:
            if j not in answer:
                answer.append(j)
    return list(map(int,answer))