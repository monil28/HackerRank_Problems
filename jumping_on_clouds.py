"""
    https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.

def jumpingOnClouds(c):
    # Write your code here
    count=0
    j=0
    while j<len(c)-1:
        if (j+2)<=len(c)-1 and c[j+2] != 1:
            count += 1
            j += 2
        else:
            count += 1
            j += 1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
