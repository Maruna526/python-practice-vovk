def read_grade(prompt):
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Error: digits only")
            continue

        grade = int(value)

        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue

        return grade


def to_letter(grade):
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    return sum(grades) / len(grades)


def count_above(grades, limit):
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    avg = average(grades)

    print("--- Report ---")
    print(f"Student: {name} Vovk, group {group}")
    print("Grades:", *grades)
    print(f"Average: {avg:.2f} -> {to_letter(avg)}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print("Above average:", count_above(grades, avg))


def main():
    name = "Maria"
    group = "I-23"
    n = len(name)

    print(f"{name} Vovk, {group}")

    grades = []

    for i in range(n):
        grade = read_grade(f"Grade {i + 1} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)


main()
