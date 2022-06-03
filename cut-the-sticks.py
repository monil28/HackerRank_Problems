"""
    https://www.hackerrank.com/challenges/cut-the-sticks/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def discard(arr):
    c = arr.count(0)
    for i in range(c):
        arr.remove(0)
    return arr

def cutTheSticks(arr,n):
    # Write your code here
    res=[n]
    while len(arr) > 1:
        min_len = min(arr)
        for j in range(n):
            arr[j] = arr[j] - min_len
        arr = discard(arr)
        n=len(arr)
        res.append(n)
    return discard(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr,n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
