# https://www.hackerrank.com/challenges/kangaroo/problem

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    p1 = x1
    p2 = x2
    d = abs(p2 - p1)
    dec = True
    while(dec):
        p1 += v1
        p2 += v2
        if p1 == p2:
            return 'YES'
        dn = abs(p2 - p1)
        if dn <= d:
            d = dn
        else:
            return 'NO'

print(kangaroo(2, 1, 1, 2))
print(kangaroo(0, 3, 4, 2))

