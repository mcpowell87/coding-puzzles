import sys
import json
from time import perf_counter

""" 1.8 Zero Matrix: Write an algorithm such that if an element in an M x N matric is 0, its entire row and column are set to 0.
"""

def zero_matrix(matrix):
    points = []

    # Find 0s
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                points.append([i, j])
    for p in points:
        matrix[p[0]] = [0 for x in matrix[p[0]]]
        for i in range(len(matrix)):
            matrix[i][p[1]] = 0
    return matrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

if __name__ == "__main__":
    if (len(sys.argv) >= 1):
        timerStart = perf_counter()
        matrix = json.loads(sys.argv[1])
        original = matrix.copy()
        print("Result:")
        printMatrix(zero_matrix(matrix))
        timerStop = perf_counter()
        print("Elapsed time: ", timerStop - timerStart)
    else:
        print("Requires one argument.")