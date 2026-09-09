name = "Maria"
surname = "Vovk"
group = "І-23"

d = 2
c = 4

print(f"{name} {surname}, {group}")

n = d * c

print(f"n = {d} * {c} = {n}")

divisors = []
divisors_sum = 0

for number in range(1, n + 1):
    if n % number == 0:
        divisors.append(number)
        divisors_sum += number

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {divisors_sum}")


if n < 2:
    print(f"{n} is not prime")
else:
    for divisor in range(2, n):
        if n % divisor == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")


primes = []

for number in range(2, n + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        primes.append(number)

print(f"Primes up to {n}:", *primes)
print(f"Primes count: {len(primes)}")
