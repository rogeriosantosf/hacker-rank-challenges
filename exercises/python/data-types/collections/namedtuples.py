
# Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
# Your task is to help Dr. Wesley calculate the average marks of the students.

# avarage = Sum of All Marks / Total of Students

# Sample Input

# TESTCASE 01

# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
# TESTCASE 02

# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5
# Sample Output

# TESTCASE 01

# 78.00

# TESTCASE 02

# 81.00

from collections import namedtuple

if __name__ == '__main__':
    students_number = int(input())
    Student = namedtuple('Student', " ".join(input().split()))
    students = []
    marks_sum = 0

    for i in range(students_number):
        students.append(Student(*input().split()))
        marks_sum += int(students[i].MARKS)

    print("{:0.2f}".format(marks_sum / students_number))
