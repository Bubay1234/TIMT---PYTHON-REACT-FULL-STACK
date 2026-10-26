students = {
    "Rahul": 75,
    "Priya": 45,
    "Amit": 88,
    "Sneha": 60,
    "Rohan": 35
}

print("Student Marks:")

for name, marks in students.items():
    print(name, ":", marks)

print("\nStudents who scored 50 or above:")

for name, marks in students.items():
    if marks >= 50:
        print(name)

highest = max(students.values())
print("\nHighest Mark:", highest)

for name, marks in students.items():
    if marks == highest:
        print("Topper:", name)
