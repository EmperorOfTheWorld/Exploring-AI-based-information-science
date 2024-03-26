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
        texts = texts + str(coef) + "x^" + str(expo) +" "
        expo = expo - 1
    return texts

coefficinet = [5, -2, 0, 6]

print(print_fx(coefficinet))
