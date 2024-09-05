def solution(data, ext, val_ext, sort_by):
    index = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    idx = index[ext]
    answer = []
    for d in data:
        if d[idx] <= val_ext:
            answer.append(d)
    answer = sorted(answer, key= lambda x: x[index[sort_by]])
    return answer