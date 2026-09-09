# Завдання 4. Вовк Марія, група І-23

score = int(input("Enter your score (0-100): "))
missed = int(input("Enter missed classes (integer): "))

if score < 0 or score > 100:
    print(f"Error: invalid score {score}")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    if missed > 16 * 0.30:
        admission = "not allowed"
    else:
        admission = "allowed"

    if grade != "F" and admission == "allowed":
        status = "passed"
    else:
        status = "failed"

    print(f"{score} points, grade {grade}, {status}")
    if admission == "not allowed":
        print("Warning: admission is not allowed because of too many missed classes")
