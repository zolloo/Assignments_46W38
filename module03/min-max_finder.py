numbers = []
print("Please type in numbers one by one.")
print("Type 'end' when you are done.\n")

while True:
    user_input = input("Enter a number (or 'end' to finish): ")
    if user_input.strip().lower() == "end":
        break
    numbers.append(float(user_input))

if len(numbers) == 0:
    minimal, maximal = None, None
else:
    minimal = numbers[0]
    maximal = numbers[0]
    for value in numbers[1:]:
        if value < minimal:
            minimal = value
        if value > maximal:
            maximal = value

print()
print(f"The list of number is: {numbers}")
print(f"The minimal number is: {minimal}")
print(f"The maximal number is: {maximal}")

