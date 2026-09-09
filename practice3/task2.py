# Завдання 2. Вовк Марія, група І-23

number = int(input("Enter an integer: "))

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

print(f"The number is {sign}")

if number != 0:
    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"The number is {parity}")
