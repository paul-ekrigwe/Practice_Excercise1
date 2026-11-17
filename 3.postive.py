n = int(input("Enter a positive whole number: "))

count = 0
even_sum = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        print(number)
        count += 1
        even_sum += number

print("Total even numbers:", count)
print("Sum of even numbers:", even_sum)