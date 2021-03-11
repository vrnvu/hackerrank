# https://www.hackerrank.com/challenges/bon-appetit/problem

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s = sum([v for i, v in enumerate(bill) if i != k]) // 2
    if s == b:
        print('Bon Appetit')
    else:
        print(b-s)

bonAppetit([3, 10, 2, 9], 1, 12)
bonAppetit([3, 10, 2, 9], 1, 7)
