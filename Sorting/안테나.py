N = int(input())
houses = list(map(int, input().split()))
houses.sort()
temp = 1e9
for house in houses:
    anthena = 0
    for j in range(len(houses)):
        anthena += abs(houses[j]-house)
    if temp != anthena:
        temp = min(temp, anthena)
        if temp == anthena:
            answer = house
print(answer)