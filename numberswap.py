a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("\nBefore swapping:")
print("A =", a)
print("B =", b)
print("C =", c)


a, b, c = b, c, a

print("\nAfter swapping:")
print("A =", a)
print("B =", b)
print("C =", c)