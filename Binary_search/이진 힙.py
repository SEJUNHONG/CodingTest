T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0
    for n in nums:
        last += 1
        heap[last] = n

        child = last
        while child // 2 and heap[child] < heap[child//2]:
            heap[child], heap[child//2] = heap[child//2], heap[child]
            child //= 2


    child = last // 2
    answer = 0
    while child:
        answer += heap[child]
        child //= 2
    print(f'#{test_case} {answer}')