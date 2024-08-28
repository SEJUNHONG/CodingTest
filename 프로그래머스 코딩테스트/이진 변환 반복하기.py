def solution(s):
    cnt = 0
    cnt_0 = 0
    while s != '1':
        cnt += 1
        num = s.count('1')
        cnt_0 += len(s) - num
        s = bin(num)[2:]
    return [cnt, cnt_0]