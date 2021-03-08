# https://www.hackerrank.com/challenges/grading/problem

def gradeStudent(grade):
    if grade == 100:
        return grade
    if grade < 38:
        return grade

    d0 = grade // 10
    d1 = grade % 10

    if d1 < 5 and d0 * 10 + 5 - grade < 3:
         return d0 * 10 + 5
    if d1 > 5 and d0 * 10 + 10 - grade < 3:
        return d0 * 10 + 10

    return grade

def gradingStudents(grades):
    # Write your code here
    return list(map(gradeStudent, grades))

r = gradingStudents([73, 67, 38, 33])

print(r)
