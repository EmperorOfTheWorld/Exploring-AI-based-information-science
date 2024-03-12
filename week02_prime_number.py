number = int(input("Input number : "))

is_prime_number = True

if number < 2:
    is_prime_number = False
else:
    i = 2
    while i*i < number:
        if number % i == 0:
            is_prime_number = False
            break
        i = i + 1

if is_prime_number == True:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")
