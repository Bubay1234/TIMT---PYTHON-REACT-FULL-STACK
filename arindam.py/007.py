# 2. Read and print the content of student.txt

with open("student.txt", "r") as file:
    content = file.read()
    print("Student Details:")
    print(content)