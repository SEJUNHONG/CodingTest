def solution(price, money, count):
    answer = 0
    time = 0
    while count != 0:
        time += 1
        if money > price * time:
            money -= price * time
        else:
            answer += price * time - money
            money = 0
        count -= 1

    return answer