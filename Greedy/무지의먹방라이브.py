from operator import itemgetter

food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    N = len(food_times)
    foods = []
    for i in range(N):
        foods.append((food_times[i], i+1))
    foods.sort()

    pretime = 0
    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * N
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= N
                sublist = sorted(foods[i:], key=itemgetter(1))
                return sublist[k][1]
        N -= 1

    return -1

print(solution(food_times, k))