dh = [0, 1, -1, 0]
dw = [1, 0, 0, -1]

def solution(board, h, w):
    n = len(board)
    count = [[0] * n for _ in range(n)]

    for i in range(4):
        w_check = w + dw[i]
        h_check = h + dh[i]
        if 0 <= w_check < n and 0 <= h_check < n:
            if board[h][w] == board[h_check][w_check]:
                count[h][w] += 1

    return count[h][w]