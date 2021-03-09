# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/


# Complete the breakingRecords function below.
def breakingRecords(scores):
    smin = scores[0]
    cmin = 0
    smax = scores[0]
    cmax = 0
    for s in scores:
        if s < smin:
            smin = s
            cmin += 1
        if s > smax:
            smax = s
            cmax += 1

    return [cmax, cmin]

r = breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
print(r)
r = breakingRecords([10,5,20,20,4,5,2,25,1])
print(r)
