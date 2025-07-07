a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

operation = "+-*/"
op = input("Enter the operator (+, -, *, /): ")

if op == '+':
    print("Sum:", a + b)
elif op == '-':
    print("Subtraction:", a - b)
elif op == '*':
    print("Multiplication:", a * b)
elif op == '/':
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division by zero!")
else:
    print("Invalid operator entered.")


