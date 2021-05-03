import sys
from time import perf_counter

""" 1.5 There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character.  Given two strings, write a function to check if 
they are one edit (or zero edits) away.
"""

def one_away(str1, str2):
    table = []

    for i in range(len(str1)+1):
        if i == 0:
            table.append([x for x in range(len(str2)+1)])
        else:
            r = [0 for x in range(len(str2)+1)]
            r[0] = i
            table.append(r)

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1
    return table[len(str1)-1][len(str2)-1] == 1

if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        timerStart = perf_counter()
        print("Result: ", one_away(sys.argv[1], sys.argv[2]))
        timerStop = perf_counter()
        print("Elapsed time: ", timerStop - timerStart)
    else:
        print("Requires two arguments.")