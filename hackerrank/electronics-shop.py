# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):
    m = -1
    for k in keyboards:
        for d in drives:
            t = k + d
            if t >= m and t <= b:
                m = t
    return m

r = getMoneySpent([40, 50, 60], [5, 8, 12], 60)
print(r)
