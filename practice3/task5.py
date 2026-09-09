# Завдання 5. Вовк Марія, група І-23

day = int(input("Day (integer): "))
month = int(input("Month (integer): "))
year = int(input("Year (integer): "))

if year <= 0:
    print(f"Date is invalid: year {year} must be positive")
elif month < 1 or month > 12:
    print(f"Date is invalid: month {month} must be from 1 to 12")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_day = 29
        else:
            max_day = 28

    if day < 1 or day > max_day:
        print(f"Date is invalid: month {month} has only {max_day} days")
    else:
        print(f"Date is valid: {day:02d}.{month:02d}.{year}")
