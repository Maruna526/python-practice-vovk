name = "Maria"
surname = "Vovk"
group = "I-23"
y = 2008


def print_age(year):
    print(f"Age: {2026 - year}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1

    age = current_year - year
    return age

    print("after return")


def main():
    print(f"{name} {surname}, {group}")

    print_age(y)

    print("print_age returned:", print_age(y))

    age = get_age(y)
    print("Age from get_age:", age)

    print("Age in months:", age * 12)
    print("Age in weeks:", age * 52)

    print("Age in 2030:", get_age(y, current_year=2030))

    print("Invalid year 3000 gives:", get_age(3000))


main()
