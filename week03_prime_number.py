def is_prime_number(n) -> bool:
        """
        prime number determination function
        :param n: a positive integer
        :return: Returns True if it is a prime number, and returns FLase if it is not a prime number.
        """
        if k < 2:
               return False
        else:
                i = 2
                while i * i <= k:
                        if k % i == 0:
                                return False
                        i = i + 1
        return True

start, end = map(int, input("Input start and end number : ").split())

for k in range(start, end+1):
        if is_prime_number(k): print(k, end=' ')


