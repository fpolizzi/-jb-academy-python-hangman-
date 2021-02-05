grades = input()
list_grades = grades.split()

grade_a = list_grades.count("A")

result = grade_a / len(list_grades)
print(round(result, 2))
