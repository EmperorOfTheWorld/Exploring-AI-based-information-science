number = int(input("Input number : "))

is_prime_number = True

if number < 2:
    is_prime_number = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime_number = False
            break

if is_prime_number == True:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")
