import math
import os
import random
import re
import sys

n = 8
s = 'UDDDUDUUDDDD'
# Complete the countingValleys function below.

def counting_valleys(n, s):
    v_count = 0
    sea_level = 0
    prev_lvl = 0
    for step in s:
        if step == 'D':
            print("into the valey")
            sea_level -=1
            if sea_level < 0 and prev_lvl >= 0:
                v_count +=1
                prev_lvl = sea_level
            elif sea_level < 0 and prev_lvl <0:
                print('still in the same valey')
        else:
            sea_level +=1
            prev_lvl = sea_level
    return v_count

print(counting_valleys(n, s))