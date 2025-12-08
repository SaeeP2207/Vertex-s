def add(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(a, b):
	return a * b
def divide(a, b):
	if b==0:
		print("Invalid")
	return a / b
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = int (input("Enter your choice(1-5): "))
match choice:
	case 1:
		a = float(input("Enter first number: "))
		b = float(input("Enter second number: "))
		print("Result: ",add(a, b))
	case 2:
		a = float(input("Enter first number: "))
		b = float(input("Enter second number: "))
		print("Result: ",subtract(a, b))
	case 3:
		a = float(input("Enter first number: "))
		b = float(input("Enter second number: "))
		print("Result: ",multiply(a, b))
	case 4:
		a = float(input("Enter first number: "))
		b = float(input("Enter second number: "))
		print("Result: ",divide(a, b))
	case 5:
		print("Exit")
	case _:
		print("Invalid") 