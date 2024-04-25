from itertools import combinations

T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    H_i = list(map(int, input().split()))
    S = sum(H_i)
    answer = sum(H_i)

    for i in range(1, N+1):
        temps = list(combinations(H_i, i))
        for temp in temps:
            if B <= sum(temp):
                answer = min(answer, sum(temp))

    print(f'#{test_case} {answer-B}')