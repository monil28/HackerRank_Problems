"""
    https://www.hackerrank.com/challenges/waiter/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def isPrime(n):
    for l in range(2,n//2+1):
        if(n%l==0):
            return(0)
    return(1)

def waiter(number, q):
    # Write your code here
    answer=[]
    prime=[]
    a1=[]
    i=2
    while(1):
        if isPrime(i):
            prime.append(i)
            if len(prime)==q:
                break
        i=i+1
               
    for j in range(q):
        for k in range(len(number)):
            if number[k] % prime[j] == 0:
                answer.append(number[k])
            else:
                a1.append(number[k])
        a1.reverse()
        number=a1.copy()
        a1.clear()
   
    for m in range(len(number)-1,-1,-1):
        answer.append(number[m])
    
    return answer
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
