#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    _original = list(s)
    _reversed =  list(s[::-1])
    _palindrome = []
    _changes = 0
    _left = 0
    _right = n - 1
    
    while(_left<_right):
        if(_original[_left] < _reversed[_left]):
            _palindrome.append(_reversed[_left])
            _changes += 1
        else:
            _palindrome.append(_original[_left])
        _left += 1
        _right -= 1
    print(_palindrome)   
    
    if(_changes > k):
        return "-1"
    
    i = 0
    # while(_changes < k):
    #     if(_palindrome[i] != '9'):
    #         _palindrome[i] = _palindrome[-1-i] = '9'
    #         _changes += 2
  
    return ''.join(_palindrome)
        
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
