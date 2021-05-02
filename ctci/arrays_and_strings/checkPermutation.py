import sys
from time import perf_counter 

""" 1.2 Given two strings, write a method to decide if one is permutation of the other. """

def checkPermutation(str1, str2):
    hash1 = {}
    hash2 = {}
    if (len(str1) != len(str2)):
        return False
    
    for c in range(max(len(str1), len(str2))):
        if (c < len(str1)):
            if (hash1.get(str1[c]) == None):
                hash1[str1[c]] = 1
            else:
                hash1[str1[c]] += 1
        if (c < len(str2)):
            if (hash2.get(str2[c]) == None):
                hash2[str2[c]] = 1
            else:
                hash2[str2[c]] += 1
    
    if (len(hash1) != len(hash2)):
        return False

    for k in hash1:
        if (hash1.get(k) != hash2.get(k)):
            return False
    
    return True

def main():
    if (len(sys.argv) > 2):
        str1 = sys.argv[1]
        str2 = sys.argv[2]
        timerStart = perf_counter() 
        print("Result: ", checkPermutation(str1, str2))
        timerStop = perf_counter()
        print("Elapsed time: ", timerStop-timerStart) 
    else:
        print("Requires two arguments.")

if __name__ == '__main__':
    main()