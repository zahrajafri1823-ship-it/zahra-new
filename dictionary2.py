grades = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    if marks >= 90:
        grades[name] = "A"
    elif marks >= 75:
        grades[name] = "B"
    else:
        grades[name] = "C"

print("Grades:")
for name, grade in grades.items():
    print(name, ":", grade)
