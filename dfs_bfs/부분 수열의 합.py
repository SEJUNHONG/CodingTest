from itertools import combinations

T = int(input())

for x in range(1, T+1):
    N, K = map(int, input().split())
    answer = 0
    A = list(map(int, input().split()))

    for i in range(1, N+1):
        for comb in combinations(A, i):
            if sum(comb) == K:
                answer += 1

    print(f'#{x} {answer}')