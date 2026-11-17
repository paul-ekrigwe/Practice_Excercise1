Password = "paulrarity"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entry = input("Enter Password: ")
    attempts += 1

    if entry == Password:
        print("Welcome")
        break

    remaining = max_attempts - attempts
    if remaining > 0:
        print("wrong pass, remaing ", remaining, "attempts")
else:
    print("Wrong")