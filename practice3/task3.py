# Завдання 3. Вовк Марія, група І-23

a = 2
b = 12
c = 4

first_number = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /, //, %, **): ").strip()
second_number = float(input("Enter the second number: "))

if operation == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result:.4f}")
elif operation == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result:.4f}")
elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result:.4f}")
elif operation == "/":
    if second_number == 0:
        print("Error: division by zero")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.4f}")
elif operation == "//":
    if second_number == 0:
        print("Error: division by zero")
    else:
        result = first_number // second_number
        print(f"{first_number} // {second_number} = {result:.4f}")
elif operation == "%":
    if second_number == 0:
        print("Error: division by zero")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result:.4f}")
elif operation == "**":
    result = first_number ** second_number
    print(f"{first_number} ** {second_number} = {result:.4f}")
else:
    print(f"Unknown operation: {operation}")
