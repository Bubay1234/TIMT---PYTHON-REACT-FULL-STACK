# The write() function is used to write data into a file.
# with open("student.txt", "w") as file:
#     file.write("Rahul\n")
#     file.write("Susmita\n")
# This creates student.txt and stores the two names in it.
# with open("student.txt", "w") as file:
#     file.write("Name: Rahul\n")
#     file.write("Course: Python")

# with open("student.txt", "r") as file:
#     data = file.read()

# print(data)

with open("student.txt", "r") as file:
    data = file.read()

print(data)
