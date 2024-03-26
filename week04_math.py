def is_prime_number(n) -> bool:
    """
    prime number determination function
    :param n: a positive integer
    :return: Returns True if it is a prime number, and returns FLase if it is not a prime number.
    """
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= k:
            if n % i == 0:
                return False
            i = i + 1
    return True

def power(b, e) -> int:
    """
    power function
    :param b: base number
    :param e: exponent number
    :return: power Result value
    """

    result = 1
    for _ in range(e):
        result = result * b
    return result

while True:
    menu = int(input("1)prime number 2)power 3)divmod 4)quit"))
    if menu == 1:
        start, end = map(int, input("Input start and end number : ").split())

        for k in range(start, end + 1):
            if is_prime_number(k): print(k, end=' ')

    elif menu == 2:
        base, exponent = map(int, input("Input baxe & exponent nimber : ").split())
        print(f"{base}^{exponent} = {base ** exponent}")

    elif menu == 3:
        dividend, divisor = map(int, input("Input dividend & divisor number : ").split())
        print(f"{dividend} // {divisor} = {dividend // divisor}")
        print(f"{dividend} % {divisor} = {dividend % divisor}")

    elif menu == 4:
        print("exit program...")
        break

    else:
        print("You are umjunsik")

