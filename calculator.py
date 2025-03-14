num 1 = float(input("Enter first number: "))
num 2 =float(input("Enter second number: "))
operation = input("Enter operation: *,/,-,+")

if operation == "*":
 result = num1 + num2
 print(f{num1} * {num2} = {result})
elif operation == "-":
 result = num1 - num2
 elif operation == "+":
 result = num1 + num2
 print(f{num1} + {num2} = {result})
 print(f{num1} - {num2} = {result})
elif operation == "/":
     if num2 != 0:
      result = num1 / num2
      print(f{num1} / {num2} = {result})
     else:
      print("Division by zero is not allowed")
else:
 print("Invalid operation":)