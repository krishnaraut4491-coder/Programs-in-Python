# Here we created a dictionary
Student_detail={"krishna":89, "nikhil":86,"shivraj":98}
# getting the input from user
name_of_student = str(input("Enter the student's name:"))
# storing the value of key
try:
    student_marks = Student_detail[name_of_student]
except KeyError or NameError:
    print("Student not found")
else:
    # printing the value of the key 
    print(f"{name_of_student}'s marks: {student_marks}")
""" Or, we can also use an if-else block instead of try except to handle the error.
if student in Student_detail:
    student_marks = Student_detail[name_of_student]
    print(f"{name_of_student}'s marks: {student_marks}")
else:
    print("Student not found")
"""