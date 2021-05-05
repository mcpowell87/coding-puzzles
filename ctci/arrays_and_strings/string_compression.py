import sys
from time import perf_counter

""" 1.6 String Compression: Implement a method to perform basic string compression
using the counts of repeated characters.  For example, the string aabcccccaaa would
become a2b1c5a3.  If the "compressed" string could not become smaller than the original
string, your method should return the original string.  You can assume the string has
only uppercase and lowercase letters (a-z).
"""

def compress(string):
    compressed = string[0]
    count = 1
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            count = count + 1
        else:
            compressed = compressed + str(count)
            compressed = compressed + string[i]
            count = 1
    compressed = compressed + str(count)
    return compressed if len(compressed) < len(string) else string
        

if __name__ == "__main__":
    if (len(sys.argv) >= 1):
        timerStart = perf_counter()
        print("Result: ", compress(sys.argv[1]))
        timerStop = perf_counter()
        print("Elapsed time: ", timerStop - timerStart)
    else:
        print("Requires one argument.")