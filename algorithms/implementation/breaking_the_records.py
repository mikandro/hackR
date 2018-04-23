from __future__ import print_function

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):

    t1=0
    t2=0

    max_score = score[0]
    min_score = score[0]

    for val in score:
        if val > max_score:
            t1 +=1
            max_score = val

        if val < min_score:
            t2 +=1
            min_score = val

    return [t1, t2]

if __name__ == '__main__':

   score = [3, 4, 21, 36, 10, 28, 35, 5, 24, 2]
   result = breakingRecords(score)
   print(result)
