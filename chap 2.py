a = 7
b = a
a = a - 13
print(a, b)
print(id(a), id(b))

b = -6
print(a, b)
print(id(a), id(b))
