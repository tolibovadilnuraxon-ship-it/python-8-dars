import csv

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    students = list(reader)

for student in students:
    print(student['ism'])

print("---")

for student in students:
    if int(student['yosh']) > 20:
        print(student['ism'])
