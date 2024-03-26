def power(b, e) -> int:
    """
    power function
    :param b: base number
    :param e: exponent number
    :return: power Result value
    """

    result = 1
    for i in range(e):
        result = result * b
    return result

base, exponent = map(int, input("Input baxe & exponent nimber : ").split())
print(f"{base}^{exponent} = {base**exponent}")
print(f"{base}^{exponent} = {pow(base, exponent)}")
print(f"{base}^{exponent} = {power(base, exponent)}")