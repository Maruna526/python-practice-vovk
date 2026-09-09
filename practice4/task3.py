name = "Maria"
surname = "Vovk"
group = "І-23"

print(f"{name} {surname}")

text = name + surname

vowels = "aeiouy"

vowel_count = 0
consonant_count = 0

for char in text:
    if char.lower() in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"Vowels: {vowel_count}, consonants: {consonant_count}")
print(f"Total letters: {len(text)}")

if vowel_count + consonant_count == len(text):
    print("Check: correct")
else:
    print("Check: incorrect")
