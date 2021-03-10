# https://www.hackerrank.com/challenges/migratory-birds/problem

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    counter = {}
    for a in arr:
        if a not in counter:
            counter[a] = 1
        else:
            counter[a] += 1
    idx = arr[0]
    s = 1
    for key, value in counter.items():
        if value > s:
            s = value
            idx = key
        elif value == s and key < idx:
            idx = key
        else:
            pass
    return idx

r = migratoryBirds([1, 4, 4, 4, 5, 3])
print(r)
r = migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
print(r)
