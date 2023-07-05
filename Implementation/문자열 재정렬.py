words = input()
word = []
num = 0
for w in words:
    if w.isalpha():
        word.append(w)
    else:
        num += int(w)

word.sort()
word.append(str(num))
print(''.join(word))