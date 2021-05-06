import sys
import json
from time import perf_counter

""" 1.7 Rotate Matrix: Given an image represented by N x N matrix, where each pixel
    in the image is represented by an integer, write a method to rotate the image by 90 degrees.
    1 2 3 4         4 5 3 1
    3 4 5 3         3 4 4 2
    5 4 3 2  ====>  1 3 5 3
    4 3 1 1         1 2 3 4
"""

def rotate_right(matrix):
    n = len(matrix)
    rotated = []
    for i in range(n):
        rotated.append([matrix[x][i] for x in range(n-1, -1, -1)])
    return rotated

def rotate_left(matrix):
    n = len(matrix)
    rotated = []
    for i in range(n-1, -1, -1):
        rotated.append([matrix[x][i] for x in range(n)])
    return rotated

def printMatrix(original, rotated):
    for i in range(len(original)):
        print(original[i], end="    ")
        print(rotated[i])
            

if __name__ == "__main__":
    if (len(sys.argv) >= 1):
        timerStart = perf_counter()
        matrix = json.loads(sys.argv[1])
        print("Rotate Right:")
        printMatrix(matrix, rotate_right(matrix))
        print("Rotate Left:")
        printMatrix(matrix, rotate_left(matrix))
        timerStop = perf_counter()
        print("Elapsed time: ", timerStop - timerStart)
    else:
        print("Requires one argument.")