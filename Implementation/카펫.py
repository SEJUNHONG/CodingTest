brown = 24 #8 #10
yellow = 24 #1 #2


def solution(brown, yellow):
    x=int((brown+4+((brown+4)**2-16*(brown+yellow))**0.5)/4)
    y=int((brown+yellow)//x)
    answer=[max(x,y), min(x,y)]
    return answer

print(solution(brown, yellow))
