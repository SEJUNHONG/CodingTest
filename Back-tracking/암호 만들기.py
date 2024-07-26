from itertools import combinations
L, C = map(int, input().split())
alpha = sorted(list(map(str, input().split())))

vowels = ['a', 'e', 'i', 'o', 'u']
answer = []

for candidate in combinations(alpha, L):
    is_vowels = False
    is_consonants = 0

    for i in candidate:
        if i in vowels:
            is_vowels = True
        else:
            is_consonants += 1

    if is_vowels == True and is_consonants >= 2:
        answer.append("".join(map(str, candidate)))

print("\n".join(answer))