n = int(input())
customers = list(map(int, input().split()))
team_jang, team_one = map(int, input().split())
answer = 0

for customer in customers:
    customer -= team_jang
    answer += 1

    if customer > 0:
        if customer % team_one == 0:
            answer += customer // team_one
        else:
            answer += customer // team_one + 1
print(answer)
