# https://cses.fi/problemset/task/1083

n = int(input())
s = sum(map(lambda x: int(x), input().split(' ')))
print((n * (n + 1)) // 2 - s)
