import json

students = {'student1': {"roll": 101, "name":"Krishna", "percent": 86.5},
            'student2': {"roll": 102, "name":"Pratik", "percent": 96.5},
            'student3': {"roll": 103, "name":"Saurabh", "percent": 95.4}}

try:
    with open("students_data.json", "r") as jsonfile:
        students_info = json.load(jsonfile)
        print(students_info)
except FileNotFoundError:
    with open("studentrs_data.json", "w") as jsonfile:
        json.dump(students, jsonfile, indent = 4)
else:
    students_info.update(students)
    with open ("student_data.json", "w") as jsonfile:
        json.dump(students_info, jsonfile, indent = 4)