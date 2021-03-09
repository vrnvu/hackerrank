# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    def factor(i):
        for aa in a:
            if i % aa != 0:
                return False
        return True

    def divide_evenly(i):
        for bb in b:
            if bb % i != 0:
                return False
        return True

    mi = a[-1]
    ma = b[0]

    r = 0
    for i in range(mi, ma + 1):
        if factor(i) and divide_evenly(i):
            r += 1
    return r

a = [2, 4]
b = [16, 32, 96]
a = [3, 4]
b = [24, 48]
r = getTotalX(a, b)
print(r)
