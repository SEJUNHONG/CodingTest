routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    camera = -30000
    routes = sorted(routes, key= lambda x: x[1])

    for route in routes:
        if route[0] > camera:
            answer += 1
            camera = route[1]
    return answer

print(solution(routes))