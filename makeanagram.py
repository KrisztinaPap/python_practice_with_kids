#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def makeAnagram(a, b):
    dict_a = Counter(a)
    dict_b = Counter(b)

    commonDict = dict_a & dict_b

    a2 = len(a) - sum(commonDict.values())
    b2 = len(b) - sum(commonDict.values())

    return a2 + b2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
