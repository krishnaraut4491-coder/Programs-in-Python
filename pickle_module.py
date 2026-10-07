import pickle

students = {'student1': {"roll": 101, "name":"Krishna", "percent": 86.5},
            'student2': {"roll": 102, "name":"Pratik", "percent": 96.5},
            'student3': {"roll": 103, "name":"Saurabh", "percent": 95.4}}

with open("pickle_module.txt", "wt") as picklefile:
    picklefile.write(str(students))

# with open("pickle.bin", "bw") as pickelfile:
#     for student in students:
#         pickle.dump(students[student], pickelfile)
# student_list = []
# with open("pickle.bin", "rb") as pf:
#     while True:
#         try:
#             data = pickle.load(pf)
#             print(data, type(data))
#             # # if block print the name when per is greater than 90
#             # if data["percent"] >= 90:
#             #     student_list.append(data["name"])
#         except EOFError as endoffile:
#             break
# # print(student_list)