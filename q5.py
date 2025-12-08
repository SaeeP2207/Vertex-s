num = int(input("Enter a number from 1 to 7: "))
if num >= 1 and num <= 7:
    match num:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
else:
    print("Invalid Input")