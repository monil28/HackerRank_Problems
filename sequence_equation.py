"""
    https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p,n):
    # Write your code here
    res=[]
    for j in range(1,n+1):
        pos = p.index(j)+1
        res.append(p.index(pos)+1)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p,n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
