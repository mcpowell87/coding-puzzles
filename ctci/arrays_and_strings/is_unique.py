import sys
from time import perf_counter

""" 1.1 Implement an algorithm to determine if a string has all unique characters. """

def is_unique(arr):
    s = set()
    for n in arr:
        s.add(n)
    return len(s) == len(arr)

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        arr = sys.argv[1].split(',')
        timerStart = perf_counter() 
        print("Result: ", is_unique(arr))
        timerStop = perf_counter()
        print("Elapsed time: ", timerStop-timerStart) 
    else:
        print("Requires at least one argument.")