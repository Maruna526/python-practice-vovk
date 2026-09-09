name = "Maria"
surname = "Vovk"
group = "I-23"
year = 2008


def print_card():
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {year}")


def print_card_args(name, surname, group="I-23", year=2008):
    print(f"{name} {surname}, {group}, {year}")


def main():
    print(f"{name} {surname}, {group}")

    print("--- no parameters, call 1 ---")
    print_card()

    print("--- no parameters, call 2 ---")
    print_card()

    print("--- no parameters, call 3 ---")
    print_card()

    print("--- positional arguments ---")
    print_card_args(name, surname, group, year)

    print("--- keyword arguments ---")
    print_card_args(year=year, group=group, surname=surname, name=name)

    print("--- mixed arguments ---")
    print_card_args(name, surname, group=group, year=year)

    print("--- default group ---")
    print_card_args(name, surname, year=year)


main()


