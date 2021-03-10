# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    r = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                r += 1
    return r

r = divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
print(r)
