def add(a, b):
#    print(">>>> add(a, b)")
    print(f"ADDING {a} + {b}")
#    print("<<<< add(a, b)")
    return a + b

def subtract(a, b):
#    print(">>>> substract(a, b)")
    print(f"SUBTRACT {a} - {b}")
#    print("<<<< substract(a, b)")
    return a - b

def multiply(a, b):
#    print(">>>> multiply(a, b)")
    print(f"MULTIPLY {a} * {b}")
#    print("<<<< multiply(a, b)")
    return a * b

def divide(a, b):
#    print(">>>> divide(a, b)")
    print(f"DIVIDING {a} / {b}")
#    print("<<<< divide(a, b)")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
# print(">>>> age =", age)
height = subtract(78, 4)
# print(">>>> height =", height)
weight = multiply(90, 2)
# print(">>>> weight =", weight)
iq = divide(100, 2)
# print(">>>> iq =", iq)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")
