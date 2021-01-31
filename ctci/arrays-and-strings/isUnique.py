import sys

""" 1.1 Implement an algorithm to determin if a string has all unique characters. """

def isUnique(arr):
    s = set()
    for n in arr:
        s.add(n)
    
    return len(s) == len(arr)

def main():
    if (len(sys.argv) > 1):
        arr = sys.argv[1].split(',')
        print(isUnique(arr))
    else:
        print("Requires at least one argument.")

if __name__ == '__main__':
    main()