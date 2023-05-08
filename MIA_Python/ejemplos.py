def gauss(A, b):
    n = len(b)
    # Matriz aumentada
    Ab = [row[:] + [col] for row, col in zip(A, b)]
    print("Matriz aumentada:")
    for row in Ab:
        print(row)
    # Eliminación hacia adelante
    for i in range(n-1):
        for j in range(i+1, n):
            factor = Ab[j][i] / Ab[i][i]
            Ab[j] = [elem - factor * Ab[i][k] for k, elem in enumerate(Ab[j])]
        print(f"Eliminación hacia adelante, paso {i+1}:")
        for row in Ab:
            print(row)
    # Sustitución hacia atrás
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i][n] - sum([Ab[i][k] * x[k] for k in range(i+1,n)])) / Ab[i][i]
    print("Sustitución hacia atrás:")
    print(x)
    return x

# Ejemplo
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]
x = gauss(A, b)