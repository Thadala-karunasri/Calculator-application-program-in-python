def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers and returns the difference."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers and returns the product."""
  return x * y

def divide(x, y):
  """Divides two numbers and returns the result, handling division by zero."""
  if y == 0:
    return "Error: Cannot divide by zero."
  else:
    return x / y

while True:
  # Get user input
  print("\nSimple Calculator")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("0. Exit")
  choice = input("Enter your choice (1/2/3/4/0): ")

  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    if choice == '1':
      result = add(num1, num2)
      print(f"{num1} + {num2} = {result}")
    elif choice == '2':
      result = subtract(num1, num2)
      print(f"{num1} - {num2} = {result}")
    elif choice == '3':
      result = multiply(num1, num2)
      print(f"{num1} * {num2} = {result}")
    else:
      result = divide(num1, num2)
      print(f"{num1} / {num2} = {result}")
  elif choice == '0':
    print("Exiting calculator.")
    break
  else:
    print("Invalid choice. Please enter a number between 0 and 4.")
