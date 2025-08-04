def plus(a,b):
    print("plus")
    return a + b
def minus(a,b):
    print("minus")
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b