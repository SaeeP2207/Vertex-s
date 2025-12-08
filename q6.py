rint("Menu:")
print("1. Add")
print("2. Subtract")
print("4. Divide")
print("5. Exit")
choice = int(input("Enter your choice (1-5): "))
if 1 <= choice <= 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    match choice:
        case 1:
            result = num1 + num2
            print("Result:", result)
            print("3. Multiply")

        case 2:
            result = num1 - num2
            print("Result:", result)

        case 3:
            result = num1 * num2
            print("Result:", result)

        case 4:
            if num2 == 0:
                print("Error: Division by zero not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)
elif choice == 5:
    print("Exit")
else:
    print("Invalid choice")