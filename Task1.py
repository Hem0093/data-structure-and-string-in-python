students = {"Alice": 85,"john":50}
name = input("Enter your students  name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found")
