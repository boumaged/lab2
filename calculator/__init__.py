def add(a, b):
   return a + b
def subtract(a, b):
   return a - b
def multiply(a, b):
   return a * b
def divide(a, b):
   if b == 0:
      raise ValueError("Cannot divide by zero.")
   return a / b
def main():
    # Example usage
    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")

if __name__ == "__main__":
    main()
