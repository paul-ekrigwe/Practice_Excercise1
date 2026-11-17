subjects = ["Python", "Security", "AI"]
#print (subjects[0:-2])
print (subjects[0])
print (subjects[1])
print (subjects[2])

NewSub = input("Enter new subject: ")
subjects.append(NewSub)
print(*subjects)

for subject in subjects:
    print(subject, sep="\n")

if "Python" in subjects:
    print("Python is in the list")
else:
    print("Python is not in the list")

print("The length of the list is: ", len(subjects))

if "math" in subjects:
    subjects.remove("math")
    print("math is in the list and has been removed")
else:
    print("math is not in the list")
print("The list after removing Security is: ", subjects)