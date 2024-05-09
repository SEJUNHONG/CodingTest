T = int(input())

def preorder(N):
    global answer
    if N:
        answer += 1
        preorder(visited1[N])
        preorder(visited2[N])

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    visited1 = [0] * (E+2)
    visited2 = [0] * (E+2)
    tree = list(map(int, input().split()))
    for i in range(0, len(tree), 2):
        parent, child = tree[i], tree[i+1]
        if visited1[parent] == 0:
            visited1[parent] = child
        else:
            visited2[parent] = child
    answer = 0
    preorder(N)

    print(f'#{test_case} {answer}')