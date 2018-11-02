import math
import os
import random
import re
import sys

s = 'abcac'
n = 14

def repeatedString(s, n):
    s_len = len(s)
    a_in_s = s.count('a')

    reps = n // s_len
    mod  = n % s_len

    if reps == 0:
        return s[0:n].count('a')

    tmp = reps * a_in_s
    if mod == 0:
        return tmp
    else:
        return tmp + s[0:mod].count('a')





result = repeatedString(s, n)

print(result)