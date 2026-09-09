# Завдання 1. Вовк Марія, група І-23

name = input("Enter your name: ").strip()
age = int(input("Enter your age (integer): "))

if not name:
    display_name = "Anonymous"
else:
    display_name = name

if age < 0:
    category = "invalid value"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"{display_name}, your category is {category}")
