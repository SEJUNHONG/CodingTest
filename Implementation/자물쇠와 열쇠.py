key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate_a_matrix_by_90_degree(a):
    N = len(a)
    M = len(a[0])
    result = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            result[j][N - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    new_lock = [[0] * (N * 3) for _ in range(N * 3)]
    for i in range(N):
        for j in range(N):
            new_lock[i+N][j+N] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(N*2):
            for y in range(N*2):
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

print(solution(key, lock))