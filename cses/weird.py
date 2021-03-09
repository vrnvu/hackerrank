# https://cses.fi/problemset/task/1068

def weird(n: int):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1, end=' ')

n = int(input())
weird(n)
