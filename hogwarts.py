# students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# For loop
# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=': ')