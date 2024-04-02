def print_fx(fx):
    texts = "f(x) = "
    expo = len(fx) - 1

    for i in range(len(fx)):
        coef = fx[i]
        if coef == 0:
            expo = expo - 1
            continue
        if ((coef >= 0)&(i!=0)):
            texts = texts + "+"
        texts = texts + f"{coef}x^{expo} "
        expo = expo - 1
    return texts

def cal(fx, x):
    expo = len(fx) - 1
    tot = 0

    for i in range(len(fx)):
        coef = fx[i]
        tot = tot + coef * x ** expo
        expo = expo - 1

    return tot

coefficient = [5, -2, 0, 6]

print(print_fx(coefficient))

x = int(input())
print(cal(coefficient ,x))