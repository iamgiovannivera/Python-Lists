#4. Deep Dive into Python Lists

# print("-----------------------")

# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]


# # Task 1
# for student, grade, activity in zip(students, grades, activities):
#     if grade < 80:
#         print(f'{student}, {grade}, {activity}')

# print("-----------------------")

# # Task 2
# students_approved = [student for student, grade in zip(students, grades) if grade >= 80]


# print("-----------------------")

# # Task 3
# print("Students approved:", students_approved)