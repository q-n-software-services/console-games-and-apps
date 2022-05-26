import numpy as np

dimension = int(input('Enter the dimension of matrix : \t'))
matrix = np.zeros((dimension, dimension))
x = int(dimension/2)
y = int(dimension/2)
if dimension % 2 == 0:
    x = x - 1
    y = y - 1

value = 1
matrix[x][y] = value
value += 1
for i in range(dimension):
    if i % 2 == 0:
        for j in range(0, i):
            y -= 1
            matrix[x][y] = value
            value += 1
        for k in range(0, i):
            x -= 1
            matrix[x][y] = value
            value += 1
    if i % 2 != 0:
        for j in range(0, i):
            y += 1
            matrix[x][y] = value
            value += 1
        for k in range(0, i):
            x += 1
            matrix[x][y] = value
            value += 1

    if i == dimension - 1:
        if x == 0:
            for j in range(dimension - 1):
                y += 1
                matrix[x][y] = value
                value += 1
        elif x == i:
            for j in range(dimension - 1):
                y -= 1
                matrix[x][y] = value
                value += 1

print(matrix)
