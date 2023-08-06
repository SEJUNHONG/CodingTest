import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

answer = 0

while len(cards) != 1:
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)
    sum_ = one + two
    answer += sum_
    heapq.heappush(cards, sum_)

print(answer)