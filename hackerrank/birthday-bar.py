# https://www.hackerrank.com/challenges/the-birthday-bar/problem

# Complete the birthday function below.
def birthday(s, d, m):
    if len(s) == 0:
        return 0
    if len(s) == 1 and s[0] == d and m == 1:
        return 1
    r = 0
    for i in range(0, len(s) - m + 1):
        current_segment_sum = 0
        for j in range(i, i + m):
            current_segment_sum += s[j]
        if current_segment_sum == d:
            r += 1
    return r

s = [1, 2, 1, 3, 2]
r = birthday(s, 3, 2)
print(r)
# s = [1, 1, 1, 1, 1]
# r = birthday(s, 3, 1)
# print(r)
# s = [4]
# r = birthday(s, 4, 1)
# print(r)
# s = [1, 2, 2, 3]
# r = birthday(s, 5, 2)
# print(r)
