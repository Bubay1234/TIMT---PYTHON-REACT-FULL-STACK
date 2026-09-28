# 3. Add course name to the same file

with open("student.txt", "a") as file:
    file.write("Course: BCA\n")


print("Course name added successfully.")