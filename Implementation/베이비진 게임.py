T = int(input())

def baby(p, idx):
    if p[idx] == 3:
        return True
    for i in (idx-2, idx-1, idx):
        if 0 <= i <= 7 and p[i] > 0 and p[i+1] > 0 and p[i+2] > 0:
            return True
    return False

for t in range(1, T+1):
    answer = 0
    cards = list(map(int, input().split()))
    p1, p2 = [0] * 10, [0] * 10
    for i in range(len(cards)):
        if i % 2 == 0:
            p1[cards[i]] += 1
            if baby(p1, cards[i]):
                answer = 1
                break
        else:
            p2[cards[i]] += 1
            if baby(p2, cards[i]):
                answer = 2
                break
    print(f'#{t} {answer}')