# Input variables
num1 = float(input("Enter first number: "))
op = input("Enter calculation operator: ")
num2 = float(input("Enter second number: "))

# Calculation functions
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid operator!")