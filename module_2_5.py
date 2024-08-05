n = input('Введите n:')
m = input('Введите m:')


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


print(get_matrix(int(n), int(m), 'value'))
