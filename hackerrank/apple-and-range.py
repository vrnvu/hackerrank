# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    def in_range(p):
        return p >= s and p <= t

    ra = sum(map(lambda apple: in_range(apple + a), apples))
    ro = sum(map(lambda orange: in_range(orange + b), oranges))

    print(ra)
    print(ro)

countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])
