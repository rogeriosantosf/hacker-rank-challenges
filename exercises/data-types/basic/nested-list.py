# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

# Sample Input:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2

# Sample Output:

# Berry
# Harry

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key=lambda student: student[1])
    lowest_grade = students[0][1]
    second_lowest_grade = None
    second_lowest_names = []

    for i in range(len(students)):
        if students[i][1] > lowest_grade:
            if second_lowest_grade == None:
                second_lowest_grade = students[i][1]
                second_lowest_names.append(students[i][0])
            elif students[i][1] == second_lowest_grade:
                second_lowest_names.append(students[i][0])

    second_lowest_names.sort()
    for name in second_lowest_names:
        print(name)
