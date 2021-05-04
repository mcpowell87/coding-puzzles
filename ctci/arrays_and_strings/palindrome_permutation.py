import sys
from time import perf_counter

""" 1.4 Given a string, write a function to check if it's a permutation of a palindrome.  
    A palindrome is a word or phrase that is the same forwards and backwards.  
    A permutation is a rearrangement of letters.  
    The palindrome does not need to be limited to just dictionary words.  
    You can ignore casing and non-letter characters. 
"""

def is_palindrome_permutation(str):
    letters = dict()

    # Construct a dictionary of letters and the number of times each appears
    for character in str:
        if str.isalpha():
            c = character.lower()
            if c in letters:
                letters[c] = letters[c] + 1
            else:
                letters[c] = 1
    
    # A palindrome exists there is at most 1 letter with an odd number of appearances
    oddCount = 0
    for l in letters.keys():
        if letters[l] % 2 != 0:
            oddCount = oddCount + 1
        if oddCount > 1:
            return False
    return True
    

if __name__ == "__main__":
    if (len(sys.argv) >= 1):
        timerStart = perf_counter()
        print("Result: ", is_palindrome_permutation(sys.argv[1]))
        timerStop = perf_counter()
        print("Elapsed time: ", timerStop - timerStart)
    else:
        print("Requires one argument.")