"""
    Problem Statement Link :- https://www.hackerrank.com/challenges/equality-in-a-array/problem?h_r=internal-search

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    res=dict()
    for j in range(len(arr)):
        res[arr[j]] = res.get(arr[j],0)+1
    return len(arr)-max(res.values())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
