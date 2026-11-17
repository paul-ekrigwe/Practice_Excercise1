student = {"Name": "John Doe", "Course": "Python", "Mark": 20}
student1 = {"Name": "Jane Doe", "Course": "AI", "Mark": 60}
print(student1["Name"], "\n", student["Course"])

if student1["Mark"] >= 50:
    print("Passed")
else:
    print("Review Required")

#update = input("Enter new mark: ")
#student["Mark"] = int(update)
#print(*student)

student1.update({"Mark": int(input("Enter new mark: "))})
print(student1)

student2 = {"Name": input("Enter new mark: "),
             "Course": input("Enter new course: "),
             "Mark": int(input("Enter new mark: "))}
Class = (student1, student2)
print(Class)