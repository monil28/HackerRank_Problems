"""
    https://www.hackerrank.com/challenges/acm-icpc-team/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#
def count_topics(a,b,m):
    c=0
    for k in range(m):
        if a[k] == '1' or b[k] == '1':
            c += 1
    return c
    
def acmTeam(topic):
    # Write your code here
    res=[]
    out=[]
    n = len(topic)
    m = len(topic[0])
    for j in range(n):
        for i in range(j+1,n):
            val=count_topics(topic[j],topic[i],m)
            res.append(val)
    max_topic=max(res)
    max_count=res.count(max_topic)
    out.append(max_topic)
    out.append(max_count)
    return out
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
