name = "Maria"
surname = "Vovk"
group = "I-23"


def get_initials(name: str, surname: str) -> str:
    """Return initials."""
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0

    for char in text:
        if char.lower() == letter.lower():
            count += 1

    return count


def count_vowels(text: str) -> int:
    """Return the number of vowels."""
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def reverse_text(text: str) -> str:
    """Return text in reverse order."""
    result = ""

    for char in text:
        result = char + result

    return result


def main():
    print(f"{name} {surname}, {group}")

    print("Initials:", get_initials(name, surname))

    c = len(surname)
    vowels = count_vowels(surname)
    consonants = c - vowels

    print("Letters in surname:", c)
    print(f"Vowels: {vowels}, consonants: {consonants}")

    for letter in "aeiou":
        print(f"{letter}:", count_letters(surname, letter=letter))

    print("Default letter 'a':", count_letters(surname))
    print("Reversed surname:", reverse_text(surname))

    print("Docstring:", count_letters.__doc__)
    print("Annotations:", count_letters.__annotations__)


main()
