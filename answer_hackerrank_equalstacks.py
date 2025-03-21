#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Calculate cumulative sums for each stack
    def calculate_cumulative_sum(stack):
        cumulative_sum = []
        total = 0
        for height in reversed(stack):
            total += height
            cumulative_sum.append(total)
        return cumulative_sum

    # Get cumulative sums for each stack
    sum1 = calculate_cumulative_sum(h1)
    sum2 = calculate_cumulative_sum(h2)
    sum3 = calculate_cumulative_sum(h3)

    # Use sets to find common heights
    common_heights = set(sum1).intersection(set(sum2)).intersection(set(sum3))

    if not common_heights:
        return 0
 
    # Return the maximum common height
    return max(common_heights)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
